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
from typing import Dict, List, Optional
import time

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Boto3 clients
bedrock = boto3.client(service_name='bedrock-runtime')
secrets_client = boto3.client('secretsmanager')

def get_github_token() -> str:
    try:
        secret = secrets_client.get_secret_value(SecretId='GithubToken')
        return json.loads(secret['SecretString'])['token']
    except ClientError as e:
        logger.error(f"Failed to retrieve GitHub token: {str(e)}")
        raise

def validate_inputs(repo_link: str, branch: str) -> None:
    if not repo_link or not isinstance(repo_link, str):
        raise ValueError("Invalid repository URL")
    if not re.match(r'^https://github.com/[\w-]+/[\w-]+/?$', repo_link):
        raise ValueError("Invalid GitHub repository URL format")
    if not branch or not isinstance(branch, str):
        raise ValueError("Invalid branch name")
    if not re.match(r'^[\w-]+$', branch):
        raise ValueError("Invalid branch name format")

def make_github_request(method: str, url: str, headers: Dict, json_data: Optional[Dict] = None, 
                       max_retries: int = 3, base_delay: float = 1.0) -> requests.Response:
    retry_count = 0
    while retry_count < max_retries:
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            else:
                response = requests.post(url, headers=headers, json=json_data, timeout=10)
            
            if response.status_code == 429:  # Rate limit exceeded
                reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                sleep_time = max(reset_time - time.time(), 0)
                logger.warning(f"Rate limit exceeded. Waiting {sleep_time} seconds")
                time.sleep(sleep_time)
                continue
                
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            retry_count += 1
            if retry_count == max_retries:
                logger.error(f"Failed after {max_retries} retries: {str(e)}")
                raise
            sleep_time = base_delay * (2 ** retry_count)
            time.sleep(sleep_time)

def fetch_repository_contents(repo_link: str, branch: str, path: str = "", 
                            exclude_folders: Optional[List[str]] = None) -> Dict[str, str]:
    repo_path = urlparse(repo_link).path.strip('/')
    api_endpoint = f"https://api.github.com/repos/{repo_path}/contents/{path}?ref={branch}"
    
    github_token = get_github_token()
    headers = {
        "Authorization": f"token {github_token}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = make_github_request('GET', api_endpoint, headers)
    
    files = {}
    for item in response.json():
        if item["type"] == "dir":
            folder_name = item["path"].split("/")[-1]
            if exclude_folders and folder_name in exclude_folders:
                logger.info(f"Skipping excluded folder: {folder_name}")
                continue
            files.update(fetch_repository_contents(repo_link, branch, item["path"], exclude_folders))
        elif item["type"] == "file":
            file_content = make_github_request('GET', item["download_url"], headers).text
            files[item["path"]] = file_content
    
    return files

# Rest of the code remains the same but with updated API calls using make_github_request
# analyze_and_remediate_code, create_new_branch, and lambda_handler functions remain unchanged
# except for using the new make_github_request function for all GitHub API calls
