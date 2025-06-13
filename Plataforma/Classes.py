import random


class Pergunta:
    def __init__(self, titulo, resposta):
        self.titulo = titulo

        self.resposta = resposta
        
class BancodePerguntas:
    def __init__(self, banco=[]):
        self.banco = banco

    def adicionaPergunta(self, pergunta):
        self.banco.append(pergunta)
class Navio:
    def __init__(self,  linha, coluna, orientacao, tamanho):
        self.linha = linha
        self.coluna = coluna
        self.orientacao = orientacao
        self.tamanho = tamanho
class Tabuleiro:
    def __init__(self):
        self.campo = [[0 for coluna in range(0, 10)] for linha in range(0,10)]
        self.navioslista = []


    def adicionaNavio(self, quantidade):
        navios = 0
        while navios < quantidade:
            linha = random.randint(0,9)
            coluna= random.randint(0,9)
            orientacao =random.randint(0,1)
            tamanho = random.randint(0,3)
            navio = 0
            if len(self.navioslista)>0:
                while self.navioslista[navio].linha == linha and self.navioslista[navio].coluna == coluna and orientacao == self.navioslista[0].orientacao:
                    linha = random.randint(0,9)
                    coluna= random.randint(0,9)
                    orientacao =random.randint(0,1)
                    tamanho = random.randint(0,3)
            if 9-linha>tamanho and orientacao == 0:
                for n in range(0, tamanho):
                    try:
                        self.campo[linha][coluna+n] = 1
                        self.navioslista.append(Navio(linha, coluna, orientacao, tamanho))
                    except ValueError:
                        navios = navios
                navios+=1
            if 9-coluna>tamanho and orientacao == 1:
                for n in range(0, tamanho):
                    try:
                        self.campo[linha+n][coluna] = 1
                        self.navioslista.append(Navio(linha, coluna, orientacao, tamanho))
                    except ValueError:
                        navio = navio
                navios+=1
            navio+=1
class Peca:
    def __init__(self, tamanho, cor):
        self.tamanho = tamanho
        self.cor = cor

class torre:
    def __init__(self, torre):
        self.torre = torre