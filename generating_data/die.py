# 08/03/2023 - Lucas Garzuze Cordeiro
# Criar uma classe que representa um dado

from random import randint

class Die:
    """Uma classe que representa um único dado"""

    def __init__(self, num_sides=6):
        """Assumindo que o dado tem 6 lados. Pode ter mais"""
        self.num_sides = num_sides
    
    def roll(self):
        """Retorna um valor aleatório entre 1 e o número de lados"""
        return randint(1, self.num_sides)