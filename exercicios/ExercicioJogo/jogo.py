class Jogo:
    def __init__(self, titulo, genero, classificacaoEtaria, preco):
        self.__titulo = titulo
        self.__genero = genero
        self.__classificacaoEtaria = classificacaoEtaria
        self.__preco = preco

    def exibirDetalhes(self):
        return print(f"\nInformações:\nTítulo - {self.__titulo}\nGênero - {self.__genero}\nClassificação Etária - {self.__classificacaoEtaria}\nPreço - {self.__preco}\n")
    def GetPreco(self):
        return self.__preco
    def getTitulo(self):
        return self.__titulo