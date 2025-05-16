class Jogador:
    def __init__(self, nickName, idJogador, bibliotecaJogos = None, saldoCarteira = 0):
        self.__nickName = nickName
        self.__idJogador = idJogador
        self.__saldoCarteira = saldoCarteira

        if bibliotecaJogos is None:
            bibliotecaJogos = []
        self.__bibliotecaJogos = bibliotecaJogos

    def exibirPerfil(self):
        print(f"Perfil do jogador {self.__nickName}:\nId do Jogador - {self.__idJogador}\nBiblioteca de Jogos:")
        for n in self.__bibliotecaJogos:
            print(n.getTitulo())
        print(f"Saldo Carteira - {self.__saldoCarteira}")

    def AdicionaSaldo(self, valor):
        self.__saldoCarteira += valor
        return print(f"Novo saldo: {self.__saldoCarteira}")
    
    def DebitaSaldo(self, valor):
        if self.__saldoCarteira< valor:
            print("Erro, saldo insuficiente")           
            return False
        else:
            self.__saldoCarteira -= valor
            print("Compra efetuada com sucesso")
            return True
    def getId(self):
        return self.__idJogador
    def getBiblioteca(self):
        return self.__bibliotecaJogos
    def AvaliarJogo(self, jogo, nota):
        jogo.ReceberAvaliacao(nota)
