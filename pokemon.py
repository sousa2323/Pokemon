class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def __str__(self):
        return self.especie   

meu_pokemon = Pokemon('fogo', 'charmander')

print(meu_pokemon)        
