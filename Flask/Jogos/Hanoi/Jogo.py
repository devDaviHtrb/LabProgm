import peca
from torre import *
class Jogo:
    def __init__(self):
        self.peca1 = peca.Peca(5, "azul")
        self.peca2 = peca.Peca(4, "amarelo")
        self.peca3 = peca.Peca(3, "verde")
        self.peca4 = peca.Peca(2, "vermelho")
        self.peca5 = peca.Peca(1, "roxo")

        self.torre1 = Torre("Torre1",[self.peca1, self.peca2, self.peca3, self.peca4, self.peca5])
        self.torre2 = Torre("Torre2")
        self.torre3 = Torre("Torre3")

        self.torres = [self.torre1.Pecas, self.torre2.Pecas, self.torre3.Pecas]

        self.movimentos = 0


    def movePeca(self, torredeOrigem, TorreDestino):
        if TorreDestino.Pecas ==[] or TorreDestino.Pecas[len(TorreDestino.Pecas)-1].tamanho > torredeOrigem.Pecas[ len(torredeOrigem.Pecas)-1].tamanho:
             TorreDestino.Pecas.append(torredeOrigem.Pecas[len(torredeOrigem.Pecas)-1])
             torredeOrigem.Pecas.pop()

             self.movimentos += 1
             print(f"{torredeOrigem.nome}->{TorreDestino.nome}")
             self.VerificaFimJogo()
        else:
            print("Erro, movimento ilegal")

    def exibirJogo(self):

        print(f"Movimentos {self.movimentos}")

        for n in self.torres:
            for i in reversed(n):
                print(i.tamanho)
            print("")

    def VerificaFimJogo(self):

        if len(self.torre2) == 5 or len(self.torre3) == 5:
            print("fim de jogo")
        else:
            return


jogo = Jogo()
jogo.exibirJogo()
jogo.movePeca(jogo.torre1, jogo.torre2)
jogo.exibirJogo()
jogo.movePeca(jogo.torre1, jogo.torre2)
jogo.exibirJogo()
jogo.movePeca(jogo.torre1, jogo.torre3)
jogo.exibirJogo()