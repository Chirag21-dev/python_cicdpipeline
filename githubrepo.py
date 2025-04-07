user = g.get_user("Shikhar82")
# List repositories
for repo in user.get_repos():
    print(f"Repository Name: {repo.name}")
