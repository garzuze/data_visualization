# 26/02/2023 - Lucas Garzuze Cordeiro

# Fazer uma visualização com as temperaturas mais altas e baixcas da cidade de Sitka
# Pegando dados de 2018

import matplotlib.pyplot as plt
from datetime import datetime
import csv

def convert_to_celsius(fahrenheit):
    """Converter fahrenheit para celsius"""
    return round((fahrenheit - 32) * (5/9), 2)

filename = r'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    max_temperature = header_row.index("TMAX")
    min_temperature = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    # Pegar as datas e as temperaturas mais altas desse arquivo
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = convert_to_celsius(int(row[max_temperature]))
        low = convert_to_celsius(int(row[min_temperature]))
        name = row[name_index]
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Gráfico com as temperaturas mais altas

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='lightcoral')
ax.plot(dates, lows, c='lightskyblue')
plt.ylim([-5, 55])
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatando o gráfico

ax.set_title(f'Temperaturas mais altas e baixas - {name}', fontsize=20)
ax.set_xlabel("", fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (C°)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()