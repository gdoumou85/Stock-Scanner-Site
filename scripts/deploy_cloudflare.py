#!/usr/bin/env python3
"""
Cloudflare Pages API Deployment Script
Uploads site files directly to Cloudflare Pages
"""

import os
import json
import zipfile
import requests
from datetime import datetime

def create_deployment_zip():
    """Create zip of _site directory"""
    site_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/_site')
    zip_path = '/tmp/site-deploy.zip'
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(site_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, site_dir)
                zipf.write(file_path, arcname)
    
    return zip_path

def deploy_to_cloudflare(api_token, account_id, project_name):
    """Deploy site to Cloudflare Pages"""
    
    # Create zip
    zip_path = create_deployment_zip()
    print(f"Created deployment zip: {zip_path}")
    
    # Upload zip via API
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}/deployments"
    
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    
    with open(zip_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Deployment successful!")
        print(f"URL: {data.get('result', {}).get('url', 'Check dashboard')}")
        return True
    else:
        print(f"❌ Deployment failed: {response.status_code}")
        print(response.text)
        return False

def main():
    """Main deployment function"""
    print(f"[{datetime.now()}] Starting Cloudflare Pages deployment...")
    
    # Get credentials from environment
    api_token = os.environ.get('CF_API_TOKEN')
    account_id = os.environ.get('CF_ACCOUNT_ID')
    project_name = os.environ.get('CF_PROJECT_NAME', 'market-pulse-scanner')
    
    if not api_token or not account_id:
        print("❌ Missing credentials. Set CF_API_TOKEN and CF_ACCOUNT_ID")
        return
    
    success = deploy_to_cloudflare(api_token, account_id, project_name)
    
    if success:
        print("✅ Site deployed successfully!")
    else:
        print("❌ Deployment failed")

if __name__ == '__main__':
    main()
