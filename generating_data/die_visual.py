# 08/03/2023 - Lucas Garzuze Cordeiro
# Simular os resultados de um dado com 6 lados sendo jogado

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Criando um D6
die = Die()

# Jogar os dados algumas vezes e armazenar numa lista
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analisando os resultados
frequencies = []

for value in range(1, die.num_sides+1):
    frequencies.append(results.count(value))

# Visualizando os resultados

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Resultado'}
y_axis_config = {'title': 'Frequencia dos resultados'}

my_layout = Layout(title='Resultados de jogar o dado 1000 vezes',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')