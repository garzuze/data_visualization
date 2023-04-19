# 18/04/2023 - Lucas Garzuze Cordeiro

# Gráfico de barrar interativo que mostra os projetos de C com mais
# estrelas no GitHub.

import requests

from plotly.graph_objs import Bar
from plotly import offline
# Fazer o chamado da API e armazenar a resposta
url = "https://api.github.com/search/repositories?q=language:c&sort=stars"
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
        'color': 'rgb(34, 134, 39)',
        'line': {'width': 1.5, 'color': 'rgb(0, 100, 0)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': "Projetos de C com mais estrelas no GitHub",
    'titlefont': {'size': 28}, 
    'xaxis': {
        'title': 'Repositório',
        'titlefont': {'size': 20},
        'tickfont': {'size': 10}
    },
    'yaxis': {
        'title': 'Estrelas',
        'titlefont': {'size': 20},
        'tickfont': {'size': 10}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='c_repos.html')