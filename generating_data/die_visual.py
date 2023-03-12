# 08/03/2023 - Lucas Garzuze Cordeiro
# Simular os resultados de um dado com 6 lados sendo jogado

from die import Die

# Criando um D6
die = Die()

# Jogar os dados algumas vezes e armazenar numa lista
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)