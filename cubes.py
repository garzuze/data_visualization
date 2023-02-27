# 25/02/2023 - Lucas Garzuze Cordeiro

# Fazer um gráfico que mostre os 5 primeiros números ao cubo

import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

# Define o título do gráfico e o nome dos eixos x e y

ax.set_title("Números ao cubo", fontsize=20)
ax.set_ylabel("Número elevado ao cubo", fontsize=10)
ax.set_xlabel("Número", fontsize=10)


plt.show()