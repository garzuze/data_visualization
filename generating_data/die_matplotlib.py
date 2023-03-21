#20/03/2023 - Lucas Garzuze Cordeiro

# Criar uma visualização com matplotlib que representa um dado sendo jogado

import matplotlib.pyplot as plt
from die import Die

# Criando um D6
die = Die()

# Jogar os dados algumas vezes e armazenar numa lista
results = [die.roll() for roll_num in range(1000)]

# Analisando os resultados
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualizando os resultados
x_values = list(range(1, die.num_sides+1))
y_values = frequencies

plt.bar(x_values, y_values)
plt.title('Resultados de jogar um D6 1000 vezes')
plt.xlabel('Resultado')
plt.ylabel('Frequencia dos resultados')
plt.show()
