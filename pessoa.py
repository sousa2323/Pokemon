from pokemon import *


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anômimo"

        self.pokemons = pokemons

    def __str__(self):
        return self.nome
    

    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)

class Player(Pessoa):
    tipo = "player"


class Inimigo(Pessoa):
    tipo = "inimigo"

meu_pokemon = PokemonFogo("charmander")
meu_pokemon2 = PokemonAgua("squirtle")

eu = Player(nome="Arthur", pokemons=[meu_pokemon, meu_pokemon2])
print(eu)
eu.mostrar_pokemons()
