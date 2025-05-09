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
from requests.exceptions import RequestException
import time
from aws_lambda_powertools.utilities import parameters

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize clients
bedrock = boto3.client(service_name='bedrock-runtime')
ssm = boto3.client('ssm')

# Constants
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
BACKOFF_FACTOR = 1.5

def get_github_token():
    try:
        token = parameters.get_secret('GITHUB_TOKEN')
        if not token:
            raise ValueError("GitHub token not found in Secrets Manager")
        return token
    except Exception as e:
        logger.error(f"Error retrieving GitHub token: {str(e)}")
        raise

def validate_inputs(repo_link, branch, file_extensions=None, folders=None):
    if not repo_link or not isinstance(repo_link, str):
        raise ValueError("Invalid repository URL")
    if not branch or not isinstance(branch, str):
        raise ValueError("Invalid branch name")
    if not re.match(r'^https?://github\.com/[\w-]+/[\w-]+/?$', repo_link):
        raise ValueError("Invalid GitHub repository URL format")
    if not re.match(r'^[\w-]+$', branch):
        raise ValueError("Invalid branch name format")

def get_github_headers():
    token = get_github_token()
    return {
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    }

def make_github_request(method, url, **kwargs):
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.request(
                method, 
                url,
                timeout=REQUEST_TIMEOUT,
                **kwargs
            )
            
            if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
                if int(response.headers['X-RateLimit-Remaining']) == 0:
                    reset_time = int(response.headers['X-RateLimit-Reset'])
                    sleep_time = max(reset_time - time.time(), 0)
                    time.sleep(sleep_time)
                    continue
                    
            response.raise_for_status()
            return response
            
        except RequestException as e:
            if attempt == MAX_RETRIES - 1:
                raise
            time.sleep(BACKOFF_FACTOR ** attempt)
            
    raise Exception("Max retries exceeded")

def fetch_repository_contents(repo_link, branch, path="", exclude_folders=None):
    validate_inputs(repo_link, branch)
    repo_path = urlparse(repo_link).path.strip('/')
    api_endpoint = f"https://api.github.com/repos/{repo_path}/contents/{path}?ref={branch}"
    
    headers = get_github_headers()
    files = {}
    
    try:
        response = make_github_request('GET', api_endpoint, headers=headers)
        
        for item in response.json():
            if item["type"] == "dir":
                folder_name = item["path"].split("/")[-1]
                if exclude_folders and folder_name in exclude_folders:
                    logger.info(f"Skipping excluded folder: {folder_name}")
                    continue
                files.update(fetch_repository_contents(repo_link, branch, item["path"], exclude_folders))
            elif item["type"] == "file":
                file_content = make_github_request('GET', item["download_url"], headers=headers).text
                files[item["path"]] = file_content
                
    except RequestException as e:
        logger.error(f"Error fetching repository contents: {str(e)}")
        raise
        
    return files

[... rest of the code remains the same but with similar improvements applied to other functions ...]

def lambda_handler(event, context):
    try:
        # Validate input event structure
        required_fields = ['agent', 'actionGroup', 'function', 'messageVersion']
        if not all(field in event for field in required_fields):
            raise ValueError(f"Missing required fields: {[f for f in required_fields if f not in event]}")
            
        agent = event['agent']
        actionGroup = event['actionGroup']
        function = event['function']
        parameters = event.get('parameters', [])
        
        # Convert parameters to properties with validation
        properties = {}
        for param in parameters:
            if not isinstance(param, dict) or 'name' not in param or 'value' not in param:
                raise ValueError(f"Invalid parameter format: {param}")
            properties[param["name"]] = param["value"]
            
        # Validate required properties
        required_props = ['repository_url', 'branch_name', 'new_remediated_branch_name']
        if not all(prop in properties for prop in required_props):
            missing = [p for p in required_props if p not in properties]
            raise ValueError(f"Missing required properties: {missing}")
            
        validate_inputs(
            properties['repository_url'],
            properties['branch_name']
        )
        
        # Execute main logic with validated inputs
        code_repo = fetch_repository_contents(
            properties['repository_url'],
            properties['branch_name'],
            exclude_folders=properties.get('folders_to_exclude')
        )
        
        remediations = analyze_and_remediate_code(
            code_repo,
            properties.get('file_extensions_to_exclude', [])
        )
        
        create_branch_event = {
            'repository_link': properties['repository_url'],
            'remediations': remediations,
            'base_branch': properties['branch_name'],
            'new_branch_name': properties['new_remediated_branch_name']
        }
        
        new_branch_name = create_new_branch(create_branch_event)
        
        return {
            'response': {
                'actionGroup': actionGroup,
                'function': function,
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
        logger.error("An error occurred", exc_info=True)
        return {
            'response': {
                'actionGroup': actionGroup,
                'function': function,
                'functionResponse': {
                    'responseBody': {
                        "TEXT": {
                            "body": f"Error: {str(e)}"
                        }
                    }
                }
            },
            'messageVersion': event['messageVersion']
        }
