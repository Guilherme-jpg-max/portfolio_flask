import os
import requests


def get_github_repos():

    github_user = 'Guilherme-jpg-max'
    token = os.getenv('GITHUB_TOKEN')

    if not token:
        raise ValueError("Token do GitHub não encontrado!")

    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/users/{github_user}/repos'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()

        # Seleção manual de repositórios pelo nome
        selected_repos = ['portfolio_flask', 'lista_tarefas', 'arquivospc']
        filtered_repos = [repo for repo in repos if repo['name'] in selected_repos]
        return filtered_repos
    else:
        return []
