import os
import requests

# Função para redirecionar ao meu git e pegar os repositorios
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

        selected_repos = ['portfolio_flask', 'lista_tarefas', 'finan-as']
        filtered_repos = [repo for repo in repos if repo['name'] in selected_repos]
        return filtered_repos
    else:
        return []
