# 13/04/2023 - Lucas Garzuze Cordeiro

# Gráfico de barrar interativo que mostra os projetos de Python com mais
# estrelas no GitHub.

import requests

from plotly.graph_objs import Bar
from plotly import offline
# Fazer o chamado da API e armazenar a resposta
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers)
print(f"Status: {r.status_code}")

# Processar os resultados
response_dict = r.json()
repo_dicts = response_dict['items']

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")

    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    labels.append(f"{owner} <br> {description}")

# Fazer uma visualização
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': "Projetos de Python com mais estrelas no GitHub",
    'titlefont': {'size': 28}, 
    'xaxis': {
        'title': 'Repositório',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Estrelas',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')