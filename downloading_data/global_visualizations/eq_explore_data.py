# 06/04/2023 - Lucas Garzuze Cordeiro

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Deixar o arquivo .json legível
# eq = abreviação de earthquake (terremoto)

# Dados de terremotos ocorridos nos últimos 30 dias
filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Extraindo todos os dicionários
all_eq_dicts = all_eq_data['features']

# Extraindo um título automático
title = all_eq_data['metadata']['title']

# Extraindo magnitudes, longitudes, latitudes e títulos para cada ponto
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])          # magnitude
    lons.append(eq_dict['geometry']['coordinates'][0]) # longitude
    lats.append(eq_dict['geometry']['coordinates'][1]) # latitude
    hover_texts.append(eq_dict['properties']['title']) # título do terremoto
    
# Mapeando os terremotos
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [4*mag for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
     }]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="terremotos_mundiais.html")