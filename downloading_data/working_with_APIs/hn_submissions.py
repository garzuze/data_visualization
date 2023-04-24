# Lucas Garzuze Cordeiro - 19/04/2023

# Fazer uma visualização das postagens com mais comentários do Hacker News
# utilzando sua API

from operator import itemgetter
import requests
from plotly import offline

# Fazer um chamado da API e armazenar a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status {r.status_code}")

# Processar as informações de cada submissão
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Fazer um chamado separado para cada submissão
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # Criar um dicionário para cada artigo
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
       # Uma excessão de um post que não aceita comentários
        continue
    else:
        submission_dicts.append(submission_dict)

# Ordenar para que as publicações com mais comentários apareçam antes na lista
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

titles, hn_urls, sub_links, comments = [], [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    titles.append(title)
    hn_url = submission_dict['hn_link']
    hn_urls.append(hn_url)
    sub_links.append(f"<a href='{hn_url}'>{title}</a>")
    comments.append(submission_dict['comments'])

# Visualização
data = [{
    'type': 'bar',
    'x': sub_links,
    'y': comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgba(255,102,0,255)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': "Postagens do Hacker News com mais comentários",
    'titlefont': {'size': 20}, 
    'xaxis': {
        'title': 'Postagem',
        'titlefont': {'size': 14},
        'tickfont': {'size': 10}
    },
    'yaxis': {
        'title': 'Comentários',
        'titlefont': {'size': 14},
        'tickfont': {'size': 10}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')