from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá escolher o Pokemon que irá lhe acompanhar nessa jornada!".format(player))

    charmander = PokemonFogo("Charmander", level=1)
    pikachu = PokemonEletrico("Pikachu", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)


    print("Você possui 3 escolhas: ")
    print("1 -", charmander)
    print("2 -", pikachu)
    print("3 -", squirtle)


    while True:
        escolha = input("Escolha seu pokemon:")

        if escolha == "1":
            player.capturar(charmander)
            break
        elif escolha == "2":
            player.capturar(pikachu)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida!")

player = Player("Arthur")
player.capturar(PokemonFogo("Charmander", level=1))

inimigo1 = Inimigo(nome="Gary",pokemons=[PokemonAgua("Squirtle", level=1)])

player.batalhar(inimigo1)
