class Jogo:
    def __init__(self, titulo, genero, classificacaoEtaria, preco, avaliacao=0, numeroAvaliacoes=0):
        self.__titulo = titulo
        self.__genero = genero
        self.__classificacaoEtaria = classificacaoEtaria
        self.__preco = preco
        self.avaliacao = avaliacao
        self.numeroAvaliacao = numeroAvaliacoes

    def exibirDetalhes(self):
        return print(f"\nInformações:\nTítulo - {self.__titulo}\nGênero - {self.__genero}\nClassificação Etária - {self.__classificacaoEtaria}\nPreço - {self.__preco}\nAvaliação:{self.avaliacao}")
    def GetPreco(self):
        return self.__preco
    def getTitulo(self):
        return self.__titulo
    def ReceberAvaliacao(self, nota):
        if  self.numeroAvaliacao<1:
            self.numeroAvaliacao += 1
            self.avaliacao = nota
        elif self.numeroAvaliacao>=1:

            self.numeroAvaliacao+=1
            self.avaliacao = (self.avaliacao*(self.numeroAvaliacao-1)+nota)/self.numeroAvaliacao
