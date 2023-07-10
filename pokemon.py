class Pokemon:

    def __init__(self, tipo, especie, level=1, nome=None):
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie    

    def __str__(self):
        return "{}({})".format(self.especie, self.level)

    def atacar(self, pokemon):
        print("{} atacou {}".format(self, pokemon))

class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))

    def dar_choque(self):
        print("Deu choque")    	

meu_pokemon = PokemonEletrico("eletrico", "pikachu")
amigo_pokemon = Pokemon("fogo", "charmander")

meu_pokemon.atacar(amigo_pokemon)
amigo_pokemon.atacar(meu_pokemon)

meu_pokemon.dar_choque()

