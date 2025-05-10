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

# Initialize a Boto3 client for Bedrock
bedrock = boto3.client(service_name='bedrock-runtime')

# Fetch the GitHub token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("GitHub authentication configuration missing")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

# Request timeout in seconds
REQUEST_TIMEOUT = 30

def validate_github_url(url):
    """Validate GitHub repository URL format"""
    parsed = urlparse(url)
    if not parsed.netloc or parsed.netloc != 'github.com':
        raise ValueError("Invalid GitHub repository URL")
    if len(parsed.path.strip('/').split('/')) != 2:
        raise ValueError("Invalid repository path format")
    return True

def validate_branch_name(branch):
    """Validate Git branch name format"""
    if not re.match(r'^[a-zA-Z0-9_\-\.\/]+$', branch):
        raise ValueError("Invalid branch name format")
    return True

def handle_rate_limit(response):
    """Handle GitHub API rate limiting"""
    if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
        if int(response.headers['X-RateLimit-Remaining']) == 0:
            reset_time = int(response.headers['X-RateLimit-Reset'])
            wait_time = reset_time - datetime.now().timestamp()
            if wait_time > 0:
                logger.warning(f"Rate limit exceeded. Waiting {wait_time} seconds")
                time.sleep(wait_time)
                return True
    return False

def github_request(method, url, **kwargs):
    """Make GitHub API requests with rate limiting and retry logic"""
    kwargs['timeout'] = REQUEST_TIMEOUT
    retries = 3
    while retries > 0:
        response = requests.request(method, url, **kwargs)
        if handle_rate_limit(response):
            continue
        response.raise_for_status()
        return response
    raise Exception("Max retries exceeded for GitHub API request")

def fetch_repository_contents(repo_link, branch, path="", exclude_folders=None):
    validate_github_url(repo_link)
    validate_branch_name(branch)
    
    repo_path = urlparse(repo_link).path.strip('/')
    api_endpoint = f"https://api.github.com/repos/{repo_path}/contents/{path}?ref={branch}"
    
    response = github_request('GET', api_endpoint, headers=headers)
    
    files = {}
    for item in response.json():
        if item["type"] == "dir":
            folder_name = item["path"].split("/")[-1]
            if exclude_folders and folder_name in exclude_folders:
                logger.info(f"Skipping excluded folder: {folder_name}")
                continue
            files.update(fetch_repository_contents(repo_link, branch, item["path"], exclude_folders))
        elif item["type"] == "file":
            file_content = github_request('GET', item["download_url"], headers=headers).text
            files[item["path"]] = file_content
    
    return files

def analyze_and_remediate_code(code_repo, non_code_exts):
    def analyze_code(code):
        prompt = f"\n\nHuman: Please analyze the following code:\n\nCode:\n{code}\n\nAssistant:"
        response = bedrock.invoke_model(
            body=json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 1000,
                "temperature": 0.5,
                "top_k": 50,
                "top_p": 0.95,
                "stop_sequences": ["\n\nHuman:"]
            }),
            modelId="anthropic.claude-v2:1",
            contentType="application/json",
            accept="*/*"
        )
        analysis = json.loads(response['body'].read()).get('completion', '').strip()
        return re.findall(r"(potential security vulnerability|code style issue|performance issue|code complexity issue|potential bug)", analysis)

    def remediate_code(code, issues):
        prompt = f"""
Human: Please fix the identified issues in the code below and return only the modified code without any explanations, summaries, or code block delimiters.

Code:
{code}

Issues identified:
{', '.join(issues)}

A:"""
        
        response = bedrock.invoke_model(
            body=json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 2000,
                "temperature": 0.7,
                "top_k": 50,
                "top_p": 0.95,
                "stop_sequences": ["\n\nHuman:"]
            }),
            modelId="anthropic.claude-v2:1",
            contentType="application/json",
            accept="*/*"
        )
        
        remediation = json.loads(response['body'].read()).get('completion', '').strip()
        remediation = re.sub(r"```[a-z]*", "", remediation).strip()
        remediation = remediation.replace("Here is the fixed code without any additional explanations or summaries:", "").strip()

        return remediation

    remediations = {}
    for file_path, file_content in code_repo.items():
        if any(file_path.endswith(ext) for ext in non_code_exts):
            logger.info(f"Skipping non-code file: {file_path}")
            continue
        issues = analyze_code(file_content)
        remediated_code = remediate_code(file_content, issues)
        remediations[file_path] = remediated_code
    return remediations

def create_new_branch(event):
    repo_link = event['repository_link']
    remediations = event['remediations']
    base_branch = event['base_branch']
    new_branch_name = event['new_branch_name']

    validate_github_url(repo_link)
    validate_branch_name(base_branch)
    validate_branch_name(new_branch_name)

    repo_path = urlparse(repo_link).path.strip('/')
    
    base_commit = github_request('GET', 
        f"https://api.github.com/repos/{repo_path}/git/refs/heads/{base_branch}", 
        headers=headers
    ).json()["object"]["sha"]
    
    if github_request('GET', 
        f"https://api.github.com/repos/{repo_path}/git/refs/heads/{new_branch_name}", 
        headers=headers
    ).status_code == 200:
        raise ValueError(f"Branch {new_branch_name} already exists.")
    
    github_request('POST',
        f"https://api.github.com/repos/{repo_path}/git/refs",
        json={"ref": f"refs/heads/{new_branch_name}", "sha": base_commit},
        headers=headers
    )
    
    blobs = []
    for file_path, remediated_code in remediations.items():
        blob_payload = {
            "content": base64.b64encode(remediated_code.encode()).decode(),
            "encoding": "base64"
        }
        blob_sha = github_request('POST',
            f"https://api.github.com/repos/{repo_path}/git/blobs",
            json=blob_payload,
            headers=headers
        ).json()["sha"]
        blobs.append({"path": file_path, "mode": "100644", "type": "blob", "sha": blob_sha})

    base_tree_sha = github_request('GET',
        f"https://api.github.com/repos/{repo_path}/git/trees/{base_commit}",
        headers=headers
    ).json()["sha"]
    
    new_tree_sha = github_request('POST',
        f"https://api.github.com/repos/{repo_path}/git/trees",
        json={"base_tree": base_tree_sha, "tree": blobs},
        headers=headers
    ).json()["sha"]
    
    new_commit_sha = github_request('POST',
        f"https://api.github.com/repos/{repo_path}/git/commits",
        json={"message": "Remediated code", "tree": new_tree_sha, "parents": [base_commit]},
        headers=headers
    ).json()["sha"]
    
    github_request('PATCH',
        f"https://api.github.com/repos/{repo_path}/git/refs/heads/{new_branch_name}",
        json={"sha": new_commit_sha},
        headers=headers
    )
    
    return new_branch_name

def lambda_handler(event, context):
    try:
        agent = event['agent']
        actionGroup = event['actionGroup']
        function = event['function']
        parameters = event.get('parameters', {})
        print(parameters)
        properties = {param["name"]: param["value"] for param in parameters}
        repo_link = properties.get('repository_url')
        branch = properties.get('branch_name')
        non_code_exts = properties.get('file_extensions_to_exclude')
        exclude_folders = properties.get('folders_to_exclude')
        new_branch_name = properties.get('new_remediated_branch_name')

        code_repo = fetch_repository_contents(repo_link, branch, exclude_folders=exclude_folders)
        remediations = analyze_and_remediate_code(code_repo, non_code_exts)

        create_branch_event = {
            'repository_link': repo_link,
            'remediations': remediations,
            'base_branch': branch,
            'new_branch_name': new_branch_name
        }
        
        new_branch_name = create_new_branch(create_branch_event)
        
        responseBody = {
            "TEXT": {
                "body": new_branch_name
            }
        }

        action_response = {
            'actionGroup': actionGroup,
            'function': function,
            'functionResponse': {
                'responseBody': responseBody
            }
        }

        final_response = {'response': action_response, 'messageVersion': event['messageVersion']}
        logger.info("Response: %s", json.dumps(final_response))

        return final_response

    except KeyError as ke:
        logger.error("Missing required parameter")
        responseBody = {
            "TEXT": {
                "body": "Missing required parameter"
            }
        }
        action_response = {
            'actionGroup': actionGroup,
            'function': function,
            'functionResponse': {
                'responseBody': responseBody
            }
        }
        final_response = {'response': action_response, 'messageVersion': event['messageVersion']}
        return final_response

    except Exception as e:
        logger.error("An error occurred", exc_info=True)
        responseBody = {
            "TEXT": {
                "body": "An error occurred while processing the request"
            }
        }
        action_response = {
            'actionGroup': actionGroup,
            'function': function,
            'functionResponse': {
                'responseBody': responseBody
            }
        }
        final_response = {'response': action_response, 'messageVersion': event['messageVersion']}
        return final_response
