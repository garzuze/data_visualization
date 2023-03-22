# 22/03/2023 - Lucas Garzuze Cordeiro
# Fazendo um gráfico com pontos aleatórios usando plotly

import plotly.express as px
from plotly import offline
from random_walk import RandomWalk

while True:
    # Fazer uma caminhada aleatória

    rw = RandomWalk(5_000)
    rw.fill_walk()

    df = px.data.medals_long()
    fig = px.scatter(df, x=rw.x_values, y=rw.y_values)
    fig.update_traces(marker_size=5)
    fig.show()

    keep_running = input("Quer fazer outra caminhada? (s ou n): ")
    if keep_running == 'n':
        break