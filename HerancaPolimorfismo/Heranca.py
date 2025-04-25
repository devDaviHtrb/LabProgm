class Animal:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        print("Som generico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

def fazer(x):
    x.emitir_som()
dog = Cachorro("Clau clau", 12)
gato = Gato("Kleber", 12)


fazer(gato)
