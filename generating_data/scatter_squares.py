import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Define o título do gráfico e o nome dos eixos x e y

ax.set_title("Números ao quadrado", fontsize=20)
ax.set_xlabel("Número", fontsize=10)
ax.set_ylabel("Número ao quadrado", fontsize=10)

# Define o alcance dos eixos x e y

ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')