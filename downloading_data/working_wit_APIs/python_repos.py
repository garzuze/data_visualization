# 13/04/2023 - Lucas Garzuze Cordeiro

import requests

# Fazer o chamado da API e armazenar a resposta
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers)
print(f"Status: {r.status_code}")

# Armazenar a resposta da API numa variável
response_dict = r.json()

# Processando os resultados
print(f"Total de repositórios {response_dict['total_count']}")

# Explorando informações sobre os resultados
repo_dicts = response_dict['items']
print(f"Repositórios retornados: {len(repo_dicts)}")

# Examimando todos os repositórios
print("\n Repositórios de Python com mais estrelas no Github")
for repo_dict in repo_dicts:
    print(f"\nNome: {repo_dict['name']}")
    print(f"Autor: {repo_dict['owner']['login']}")
    print(f"Estrelas: {repo_dict['stargazers_count']}")
    print(f"Repositório: {repo_dict['html_url']}")
    print(f"Criado em: {repo_dict['created_at']}")
    print(f"Atualizado em: {repo_dict['updated_at']}")
    print(f"Descrição: {repo_dict['description']}")