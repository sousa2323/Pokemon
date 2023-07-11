import random

class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level: 
            self.level = level
        else:
            self.level = random.randint(1, 100)
            
        if nome:
            self.nome = nome
        else:
            self.nome = especie 

    def __str__(self):
        return "{}({})".format(self.especie, self.level)

    def atacar(self, pokemon):
        print("{} atacou {}".format(self, pokemon))

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabeça de {}".format(self, pokemon))

class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        print("{} lançou um jato d'água em {}".format(self, pokemon))
