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

eu = Player("Arthur")

pokemon_selvagem = PokemonEletrico("Pikachu")

print("Antes de capturar")
eu.mostrar_pokemons()

eu.capturar(pokemon_selvagem)

eu.mostrar_pokemons()
