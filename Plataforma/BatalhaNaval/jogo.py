from tabuleiro import *
import random
class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.adicionaNavio(random.randint(0,9), random.randint(0,9), random.randint(0,1), random.randint(1,3))
        self.tabuleiro.adicionaNavio(random.randint(0,9), random.randint(0,9), random.randint(0,1), random.randint(1,3))
        self.tabuleiro.adicionaNavio(random.randint(0,9), random.randint(0,9), random.randint(0,1), random.randint(1,3))
        self.tabuleiro.adicionaNavio(random.randint(0,9), random.randint(0,9), random.randint(0,1), random.randint(1,3))
        self.tabuleiro.exibirTabuleiro()

        Vitoria = False
        while Vitoria == False:
            self.Jogar()
            Vitoria = True
            for n in self.tabuleiro.campo:
                for h in n:
                    if h == 1:
                        Vitoria == False

    def Jogar(self):
        self.tabuleiro.Atira(int(input("Digite a coluna que quer acertar")), int(input("Digite a linha que quer acertar")))
jogo = Jogo()
