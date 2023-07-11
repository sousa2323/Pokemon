import random

from pokemon import *

NOMES = [
    "Arthur", "Lucas", "João",
    "Maria", "José", "Pedro",
    "Paulo", "Ana", "Luiza",
    "Beatriz", "Carlos", "Cristina"
]

POKEMONS = [
    PokemonEletrico("Pikachu"),
    PokemonFogo("Charmander"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Bulbassauro"),
    PokemonEletrico("Raichu"),
    PokemonFogo("Charmeleon"),
    PokemonAgua("Wartortle"),
    PokemonAgua("Ivysaur"),
    PokemonEletrico("Pichu"),
    PokemonFogo("Charizard"),
    PokemonAgua("Blastoise"),
    PokemonAgua("Venusaur"),
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

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choices(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

meu_inimigo = Inimigo(nome="Gary")

print(meu_inimigo)
meu_inimigo.mostrar_pokemons()
