import random

from pokemon import *

NOMES = [
    "Arthur", "Lucas", "João",
    "Maria", "José", "Pedro",
    "Paulo", "Ana", "Luiza",
    "Beatriz", "Carlos", "Cristina"
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome
    

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não tem nenhum pokemon".format(self))    
class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self):
        pass

eu = Player()
print(eu)
