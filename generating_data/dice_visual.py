# 12/03/2023 - Lucas Garzuze Cordeiro
# Simular os resultados de dois dados com 6 lados sendo jogados

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Criando dois dados D6
die_1 = Die()
die_2 = Die()

# Jogar os dados algumas vezes e armazenar numa lista
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisando os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

# (a lista começa no dois pois é o menor resultado possível rolando 2 dados)
for value in range(2, max_result+1):
    frequencies.append(results.count(value))

# Visualizando os resultados

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Resultado', 'dtick': 1}
y_axis_config = {'title': 'Frequencia dos resultados'}

my_layout = Layout(title='Resultados de jogar dois dados D6 1000 vezes',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')