# 23/02/2023 - Lucas Garzuze Cordeiro

# Fazer uma visualização com os dados do tempo da cidade de Sitka
# Pegando dados de 07/2018
import matplotlib.pyplot as plt
from datetime import datetime
import csv

filename = r'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Pegar as temperaturas mais altas
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Gráfico com as temperaturas mais altas

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Formatando o gráfico

ax.set_title('Temperaturas diárias mais altas em Sitka (07/2018)', fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperatura (Fº)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()