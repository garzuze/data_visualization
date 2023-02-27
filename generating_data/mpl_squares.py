import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = (1, 4, 9, 16, 25)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

# Define o título do gráfico e o nome dos eixos x e y

ax.set_title("Números ao quadrado", fontsize=20)
ax.set_xlabel("Número", fontsize=10)
ax.set_ylabel("Número ao quadrado", fontsize=10)

# Definindo o tamanho dos números dos eixos
# "Set size of tick labels"

ax.tick_params(axis='both', labelsize=10)

plt.show()