# 06/04/2023 - Lucas Garzuze Cordeiro

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Deixar o arquivo .json legívelp
# eq = abreviação de earthquake (terremoto)

filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Extraindo todos os dicionários e verificando quantos dicionários existem
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extraindo magnitudes, longitudes e latitudes
mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']          # magnitude
    lon = eq_dict['geometry']['coordinates'][0] # longitude
    lat = eq_dict['geometry']['coordinates'][1] # latitude
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Mapeando os terremotos

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [4*mag for mag in mags],
    }
     }]

my_layout = Layout(title='Terremotos globais')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="terremotos_mundiais.html")