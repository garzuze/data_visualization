# 27/02/2023 - Lucas Garzuze Cordeiro
# Fazendo como se fosse o caminho de um grão de pólen numa gota d'água

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Fazer uma caminhada aleatória
    rw = RandomWalk()
    rw.fill_walk()

    # Coloca os pontos em um gráfico:
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.y_values, rw.x_values, linewidth=0.1)
    
    # Remover os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Quer fazer outra caminhada? (s ou n): ")
    if keep_running == 'n':
        break