import random

from pokemon import *

NOMES = [
    "Arthur", "Lucas", "João",
    "Maria", "José", "Pedro",
    "Paulo", "Ana", "Luiza",
    "Beatriz", "Carlos", "Cristina",
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
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem nenhum pokemon".format(self))
    
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido")

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))
        
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break
    
        else:
            print("essa batalha não pode ocorrer")    

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = input("Escolha seu pokemon:")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido")

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choices(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)
