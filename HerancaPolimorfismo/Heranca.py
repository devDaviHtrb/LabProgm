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
fazer(dog)


from abc import ABC, abstractmethod

class formaGeometrica(ABC):
    @abstractmethod
    def perimetro():
        pass

    @abstractmethod
    def area():
        pass

class Retangulo(formaGeometrica):
    def __init__(self, altura, largura):
        self.altura= altura
        self.largura= largura

    def perimetro(self):
        return (2*self.altura+2*self.largura)
    
    def area(self):
        return(self.altura*self.largura)
class Triangulo(formaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 =  float(lado1)
        self.lado2 =float(lado2)
        self.lado3 = float(lado3)
    def perimetro(self):
        return float(self.lado3 + self.lado2+self.lado1)
    def area(self):
        s = (self.perimetro())/2
        a = (s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))**(1/2)
        return a
       
ret= Retangulo(8, 3)
tri = Triangulo(3,4,5)

print(f"Área retângulo: {ret.area()}")
print(f"Perímetro retângulo: {ret.perimetro()}")
print(f"Área Triangulo: {tri.area()}")
print(f"Perímetro Triangulo: {tri.perimetro()}")


class Veiculo(ABC):
    @abstractmethod
    def __init__(self, modelo, marca):
        self.modelo = modelo 
        self.marca = marca
    @abstractmethod
    def exibir_detalhes(self):
        print(f"modelo:{self.modelo}\nmarca:{self.marca}")


class Moto(Veiculo):
    def __init__(self, modelo, marca, cilindradas):
        self.modelo = modelo 
        self.marca = marca
        self.cilindradas = cilindradas
    def exibir_detalhes(self):
         print(f"modelo:{self.modelo}\nmarca:{self.marca}\n cilindradas:{self.cilindradas}")

class Carro(Veiculo):
    def __init__(self, modelo, marca, num_portas):
        self.modelo = modelo 
        self.marca = marca
        self.num_portas = num_portas
    def exibir_detalhes(self):
         print(f"modelo:{self.modelo}\nmarca:{self.marca}\n num_portas:{self.num_portas}")

c = Carro("Nike", "Adidas", 4)
c.exibir_detalhes()
m = Moto("Adidas", "Nike", 22)
m.exibir_detalhes()

