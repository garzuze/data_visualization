# 25/12/2023 - Lucas Garzuze Cordeiro

# Criando um módulo que gera caminhos (pontos) aleatórios
# Pego de exemplo do livro Python Crash Course

from random import choice

class RandomWalk:
    """Uma classe que gera caminhos aleatórios"""

    def __init__(self, num_points=5000):
        """Inicializa os atributos da caminhada"""
        self.num_points= num_points

        # Todos os caminhos começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos os pontos no caminho"""

        # Continue andando até que a caminhada atinga o tamanho desejado
        while len(self.x_values) < self.num_points:

            # Decide em qual direção ir e quão longe ir
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejeita movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                continue
            
            # Calcula a nova posição
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)