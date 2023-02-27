# 25/02/2023 até 27/02/2023 - Lucas Garzuze Cordeiro
# Acompanhando um exemplo do livro

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Fazer uma caminhada aleatória

    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Coloca os pontos em um gráfico:
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
               edgecolors='none', s=5)
    
    # Emfatizar o primeiro e o último ponto:
    ax.scatter(0, 0, c='green', edgecolors='none', s=100) # Tds começam no 0
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
    s=100)

    # Remover os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Quer fazer outra caminhada? (s ou n): ")
    if keep_running == 'n':
        break