# 16/03/2023 - Lucas Garzuze Cordeiro

# Jogar dois dados D6, mas ao invés de somar seus valores, multiplicá-los
# Criar uma visualização do resultado

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Criando dois D6s
die_1 = Die()
die_2 = Die()

# Jogar os dados algumas vezes e armazenar numa lista
results = [die_1.roll() * die_2.roll() for roll_num in range(50_000)]

# Analisando os resultados
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# Visualizando os resultados
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Resultado', 'dtick': 1}
y_axis_config = {'title': 'Frequencia dos resultados'}

my_layout = Layout(title='Resultados de jogar dois dados D6 50000 vezes,'
                   'multiplicando seus resultados',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='multiplication.html')