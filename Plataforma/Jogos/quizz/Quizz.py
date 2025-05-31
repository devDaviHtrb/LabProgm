
from Db import BancodePerguntas
from Pergunta import Pergunta
class Jogo:
    def __init__(self, banco):
        self.banco = banco
        self.Jogar()

    def Jogar(self):
        for pergunta in self.banco:
            print(pergunta.titulo)
            print(pergunta.texto)
            resp = input("Verdadeiro ou falso? T/F")
            print("Correto") if resp == pergunta.resposta else print("Errado")
            resp = input("Continuar jogando? S/N")
            if resp != "S":
                break
