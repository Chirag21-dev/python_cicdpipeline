GITHUB_API_URL = "https://api.github.com"
GITHUB_USERNAME = "Chirag21-dev"  # Replace with your GitHub organization name
TOKEN = "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"  # Replace with your GitHub token
USER_TO_REMOVE = "yaswant24"  # User to be removed

#Get all the repository list in your organization
def get_repositories():
    """Get all repositories in the organization."""
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'
    #Call the REST API 
    response = requests.get(url, auth=('Chirag21-dev', TOKEN))  # Replace 'username' with your GitHub username
    #If response code is 200 , your call is success
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve repositories: {response.status_code} - {response.text}")
        return []
