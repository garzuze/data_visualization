# 27/02/2023 - Lucas Garzuze Cordeiro

# Fazer uma visualização com as temperaturas mais altas e baixas do Vale da Morte
# Pegando dados de 2018

import matplotlib.pyplot as plt
from datetime import datetime
import csv

def convert_to_celsius(fahrenheit):
    """Converter fahrenheit para celsius"""
    return round((fahrenheit - 32) * (5/9), 2)

filename = r'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    max_temperature = header_row.index("TMAX")
    min_temperature = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    # Pegar as datas e as temperaturas mais altas e baixas desse arquivo
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        name = row[name_index]
        try:
            high = convert_to_celsius(int(row[max_temperature]))
            low = convert_to_celsius(int(row[min_temperature]))
        except ValueError:
            print(f"Faltando dados para {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Gráfico com as temperaturas mais altas e baixas
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='lightcoral')
ax.plot(dates, lows, c='lightskyblue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatando o gráfico
title = f'Temperaturas  altas e baixas - {name}'
ax.set_title(title, fontsize=18)
ax.set_xlabel("", fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (C°)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()