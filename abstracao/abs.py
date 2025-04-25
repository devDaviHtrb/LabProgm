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
    
ret= Retangulo(8, 3)

print(f"Área retângulo: {ret.area()}")
print(f"Perímetro retângulo: {ret.perimetro()}")