# 10/04/2023 - Lucas Garzuze Cordeiro

# Fazer uma visualização com dados de incêndios no mundo todo.
# Dados extraídos de: https://firms.modaps.eosdis.nasa.gov/active_fire/#firms-txt

import csv
from plotly.graph_objs import Scattergeo, Layout
from datetime import datetime
from plotly import offline

filename = r'data/world_fires_1_day_2023.csv'

# Só vou fazer até a linha  10 mil que se não fica muito pesado
max_row = 10_000

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lat = header_row.index('latitude')
    lon = header_row.index('longitude')
    bright = header_row.index('brightness')
    time = header_row.index('acq_date')

    # Pegando a localização, a intensidade e a identificação de cada incêncio
    lats, lons, brightness, hover_texts = [], [], [], []
    row_number = 0

    for row in reader:
        date = datetime.strptime(row[time], '%Y-%m-%d')
        lats.append(float(row[lat]))
        lons.append(float(row[lon]))
        brightness.append(float(row[bright]))

        label = f"{date.strftime('%d/%m/%y')}- {float(row[bright])}"
        hover_texts.append(label)

        row_number += 1
        if row_number == max_row:
            break

# Mapeando os incêndios
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        # é preciso diminuir a luminosidade, pois se não os pontos ficam imensos
        'size': [bright * 0.02 for bright in brightness],
        'color': brightness,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Intensidade'}
    }
     }]

my_layout = Layout(title="Incêndios ocorridos no mundo, 1 dia <br>Fonte: "
"<a href='https://firms.modaps.eosdis.nasa.gov/active_fire/#firms-txt'>NASA</a>")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="world_fires.html")