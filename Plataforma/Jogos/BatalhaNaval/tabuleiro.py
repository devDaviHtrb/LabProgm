import Navio

class Tabuleiro:
    def __init__(self):
        self.campo = [[0 for coluna in range(0, 10)] for linha in range(0,10)]
        self.tabuleiro = [["O" for coluna in range(0, 10)] for linha in range(0,10)]
        self.navios = []


    def exibirTabuleiro(self):
        for n in self.tabuleiro:
            print(n) 
        print("\n")

    def adicionaNavio(self, linha, coluna, orientacao, tamanho):
        Possivel = True
        for h in self.navios:
            if h.linha == linha and h.coluna == coluna and orientacao == h.orientacao:
                Possivel = False
                return Possivel
        
        if Possivel == True:
            self.navios.append(Navio.Navio(linha, coluna, orientacao, tamanho))
            if 10-linha>=tamanho and orientacao == 0:#Horizontal
                for n in range(0, tamanho):
                    self.campo[linha][coluna+n] = 1
            if 10-coluna>=tamanho and orientacao == 1:#Horizontal
                for n in range(0, tamanho):
                    self.campo[linha+n][coluna] = 1
            else:
                return False
                
    def Atira(self, x, y):
        if x<=10 and y<=10:
            if self.campo[y-1][x-1] == 1:
                self.campo[y-1][x-1] = 2
                self.tabuleiro[y-1][x-1] = "X"
                return print("Navio acertado")
            else:
                return print("Água acertada")
        else:
            print("Jogada invalida")

