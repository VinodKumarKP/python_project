import json
import logging
import base64
import os
import boto3
import re
import requests
from urllib.parse import urlparse
from datetime import datetime
from botocore.exceptions import ClientError

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Boto3 clients
bedrock = boto3.client(service_name='bedrock-runtime')
secrets_manager = boto3.client('secretsmanager')

def get_github_token():
    try:
        secret = secrets_manager.get_secret_value(SecretId='GITHUB_TOKEN')
        return json.loads(secret['SecretString'])['token']
    except ClientError as e:
        logger.error(f"Error retrieving GitHub token: {e}")
        raise

def validate_github_url(url):
    parsed = urlparse(url)
    if not parsed.netloc or parsed.netloc != 'github.com':
        raise ValueError("Invalid GitHub repository URL")
    if not re.match(r'^/[\w-]+/[\w-]+/?$', parsed.path):
        raise ValueError("Invalid repository path format")

def validate_branch_name(branch):
    if not re.match(r'^[\w-]+$', branch):
        raise ValueError("Invalid branch name format")

class GitHubAPI:
    def __init__(self, token):
        self.headers = {
            "Authorization": f"token {token}",
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
        self.timeout = 10

    def _make_request(self, method, url, **kwargs):
        retries = 0
        max_retries = 3
        base_delay = 1

        while retries < max_retries:
            try:
                response = self.session.request(
                    method, 
                    url, 
                    headers=self.headers, 
                    timeout=self.timeout,
                    **kwargs
                )
                
                if response.status_code == 403 and 'rate limit' in response.text.lower():
                    retry_after = int(response.headers.get('Retry-After', base_delay * (2 ** retries)))
                    logger.warning(f"Rate limited. Waiting {retry_after} seconds")
                    time.sleep(retry_after)
                    retries += 1
                    continue
                
                response.raise_for_status()
                return response.json() if response.text else None
                
            except requests.exceptions.RequestException as e:
                if retries == max_retries - 1:
                    raise
                retries += 1
                time.sleep(base_delay * (2 ** retries))
                
def fetch_repository_contents(github_api, repo_link, branch, path="", exclude_folders=None):
    repo_path = urlparse(repo_link).path.strip('/')
    api_endpoint = f"https://api.github.com/repos/{repo_path}/contents/{path}?ref={branch}"
    contents = github_api._make_request('GET', api_endpoint)
    
    files = {}
    for item in contents:
        if item["type"] == "dir":
            folder_name = item["path"].split("/")[-1]
            if exclude_folders and folder_name in exclude_folders:
                logger.info(f"Skipping excluded folder: {folder_name}")
                continue
            files.update(fetch_repository_contents(github_api, repo_link, branch, item["path"], exclude_folders))
        elif item["type"] == "file":
            file_content = github_api._make_request('GET', item["download_url"])
            files[item["path"]] = file_content
    
    return files

def analyze_and_remediate_code(code_repo, non_code_exts):
    # [Previous implementation remains the same]
    pass

def create_new_branch(github_api, event):
    repo_link = event['repository_link']
    remediations = event['remediations']
    base_branch = event['base_branch']
    new_branch_name = event['new_branch_name']

    validate_github_url(repo_link)
    validate_branch_name(base_branch)
    validate_branch_name(new_branch_name)

    repo_path = urlparse(repo_link).path.strip('/')
    
    base_ref = github_api._make_request('GET', f"https://api.github.com/repos/{repo_path}/git/refs/heads/{base_branch}")
    base_commit = base_ref["object"]["sha"]

    # Check if branch exists
    try:
        github_api._make_request('GET', f"https://api.github.com/repos/{repo_path}/git/refs/heads/{new_branch_name}")
        raise ValueError(f"Branch {new_branch_name} already exists.")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code != 404:
            raise

    # Create new branch
    github_api._make_request(
        'POST',
        f"https://api.github.com/repos/{repo_path}/git/refs",
        json={"ref": f"refs/heads/{new_branch_name}", "sha": base_commit}
    )

    # Create blobs and tree
    blobs = []
    for file_path, remediated_code in remediations.items():
        blob_payload = {
            "content": base64.b64encode(remediated_code.encode()).decode(),
            "encoding": "base64"
        }
        blob = github_api._make_request(
            'POST',
            f"https://api.github.com/repos/{repo_path}/git/blobs",
            json=blob_payload
        )
        blobs.append({"path": file_path, "mode": "100644", "type": "blob", "sha": blob["sha"]})

    base_tree = github_api._make_request(
        'GET',
        f"https://api.github.com/repos/{repo_path}/git/trees/{base_commit}"
    )
    new_tree = github_api._make_request(
        'POST',
        f"https://api.github.com/repos/{repo_path}/git/trees",
        json={"base_tree": base_tree["sha"], "tree": blobs}
    )

    # Create commit
    new_commit = github_api._make_request(
        'POST',
        f"https://api.github.com/repos/{repo_path}/git/commits",
        json={
            "message": "Remediated code",
            "tree": new_tree["sha"],
            "parents": [base_commit]
        }
    )

    # Update branch reference
    github_api._make_request(
        'PATCH',
        f"https://api.github.com/repos/{repo_path}/git/refs/heads/{new_branch_name}",
        json={"sha": new_commit["sha"]}
    )

    return new_branch_name

def lambda_handler(event, context):
    try:
        # Validate required event parameters
        required_params = ['agent', 'actionGroup', 'function', 'parameters']
        if not all(param in event for param in required_params):
            raise ValueError(f"Missing required parameters: {[param for param in required_params if param not in event]}")

        # Initialize GitHub API client
        github_token = get_github_token()
        github_api = GitHubAPI(github_token)

        # Process parameters
        parameters = event.get('parameters', {})
        properties = {param["name"]: param["value"] for param in parameters}
        
        # Validate required properties
        required_props = ['repository_url', 'branch_name', 'new_remediated_branch_name']
        if not all(prop in properties for prop in required_props):
            raise ValueError(f"Missing required properties: {[prop for prop in required_props if prop not in properties]}")

        code_repo = fetch_repository_contents(
            github_api,
            properties['repository_url'],
            properties['branch_name'],
            exclude_folders=properties.get('folders_to_exclude')
        )

        remediations = analyze_and_remediate_code(
            code_repo,
            properties.get('file_extensions_to_exclude', [])
        )

        new_branch_name = create_new_branch(github_api, {
            'repository_link': properties['repository_url'],
            'remediations': remediations,
            'base_branch': properties['branch_name'],
            'new_branch_name': properties['new_remediated_branch_name']
        })

        return {
            'response': {
                'actionGroup': event['actionGroup'],
                'function': event['function'],
                'functionResponse': {
                    'responseBody': {
                        "TEXT": {
                            "body": new_branch_name
                        }
                    }
                }
            },
            'messageVersion': event['messageVersion']
        }

    except Exception as e:
        logger.error("An error occurred: %s", e, exc_info=True)
        return {
            'response': {
                'actionGroup': event.get('actionGroup', ''),
                'function': event.get('function', ''),
                'functionResponse': {
                    'responseBody': {
                        "TEXT": {
                            "body": f"Error: {str(e)}"
                        }
                    }
                }
            },
            'messageVersion': event.get('messageVersion', '1.0')
        }
