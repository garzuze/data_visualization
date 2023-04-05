# 26/02/2023 - Lucas Garzuze Cordeiro

# Fazer uma visualização com a precipitação cidade de Sitka
# Pegando dados de 2018

import matplotlib.pyplot as plt
from datetime import datetime
import csv

filename = r'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    prcp = header_row.index("PRCP")
    name_index = header_row.index("NAME")

    # Pegar a precipitação
    dates, precipitation = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        rainfall = float(row[prcp])
        name = row[name_index]
        precipitation.append(rainfall) 

# Gráfico com a precipitação diária

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitation, c='lightskyblue')

# Formatando o gráfico

ax.set_title(f'Precipitação diária - {name}', fontsize=20)
ax.set_xlabel("", fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Precipitação (mm)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()