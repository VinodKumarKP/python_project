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

# Initialize AWS clients
bedrock = boto3.client(service_name='bedrock-runtime')
secrets_manager = boto3.client('secretsmanager')

def get_github_token() -> str:
    try:
        secret = secrets_manager.get_secret_value(SecretId='github/api_token')
        return json.loads(secret['SecretString'])['token']
    except ClientError as e:
        logger.error(f"Failed to retrieve GitHub token: {e}")
        raise

def validate_inputs(repo_link: str, branch: str) -> None:
    if not re.match(r'^https://github\.com/[\w-]+/[\w-]+/?$', repo_link):
        raise ValueError("Invalid repository URL format")
    if not re.match(r'^[\w-]+$', branch):
        raise ValueError("Invalid branch name format")

class RateLimiter:
    def __init__(self, calls: int, period: int):
        self.calls = calls
        self.period = period
        self.timestamps = []

    def wait_if_needed(self):
        now = time.time()
        self.timestamps = [ts for ts in self.timestamps if now - ts < self.period]
        
        if len(self.timestamps) >= self.calls:
            sleep_time = self.period - (now - self.timestamps[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        self.timestamps.append(now)

# GitHub API rate limiter (5000 requests per hour)
github_rate_limiter = RateLimiter(calls=5000, period=3600)

def fetch_repository_contents(
    repo_link: str, 
    branch: str, 
    path: str = "", 
    exclude_folders: Optional[List[str]] = None,
    max_depth: int = 10,
    max_file_size: int = 1024 * 1024  # 1MB
) -> Dict[str, str]:
    if max_depth < 0:
        logger.warning(f"Max depth reached at path: {path}")
        return {}

    github_rate_limiter.wait_if_needed()
    
    repo_path = urlparse(repo_link).path.strip('/')
    api_endpoint = f"https://api.github.com/repos/{repo_path}/contents/{path}?ref={branch}"
    
    headers = {
        "Authorization": f"token {get_github_token()}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(api_endpoint, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch repository contents: {e}")
        raise

    files = {}
    for item in response.json():
        if item["type"] == "dir":
            folder_name = item["path"].split("/")[-1]
            if exclude_folders and folder_name in exclude_folders:
                logger.info(f"Skipping excluded folder: {folder_name}")
                continue
            files.update(fetch_repository_contents(
                repo_link, 
                branch, 
                item["path"], 
                exclude_folders,
                max_depth - 1
            ))
        elif item["type"] == "file":
            if item["size"] > max_file_size:
                logger.warning(f"Skipping large file: {item['path']}")
                continue
                
            github_rate_limiter.wait_if_needed()
            try:
                file_content = requests.get(item["download_url"], headers=headers)
                file_content.raise_for_status()
                files[item["path"]] = file_content.text
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch file content: {e}")
                continue

    return files

[... Rest of the code remains the same except for using the new get_github_token() function 
    and adding proper error handling in create_new_branch() and other functions ...]

def lambda_handler(event, context):
    try:
        validate_inputs(event.get('repository_url'), event.get('branch_name'))
        
        # Rest of the lambda_handler implementation remains the same
        
    except ValueError as ve:
        logger.error(f"Validation error: {str(ve)}")
        return create_error_response(event, str(ve))
    except Exception as e:
        logger.error("An error occurred: %s", e, exc_info=True)
        return create_error_response(event, str(e))
