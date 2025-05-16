class Plataforma:
    def __init__(self, nomePlataforma, catalogoJogos = list(), jogadoresCadastrados = list()):
        self.__nomePlataforma = nomePlataforma
        self.__catalogoJogos = catalogoJogos
        self.__jogadoresCadastrados = jogadoresCadastrados
    
    def adicionarJogoCatalogo(self, jogo):
        return self.__catalogoJogos.append(jogo)

    def adicionarJogador(self, jogador):
        return self.__jogadoresCadastrados.append(jogador)
    
    def buscarJogo(self, titulo):
        for jogos in self.__catalogoJogos:
            if jogos.getTitulo() == titulo:
                return jogos
        return None
    
    def buscarId(self, id):
        for jogador in self.__jogadoresCadastrados:
            if jogador.getId() == id:
                return jogador
        return None
    
    def listarCatalogo(self):
        for jogo in self.__catalogoJogos:
            jogo.exibirDetalhes()

    def AdicionarJogoBiblioteca(self, jogo, jogador):
        return jogador.getBiblioteca().append(jogo)

    def ComprarJogo(self, jogo, comprador, remetente):
        transacao = comprador.DebitaSaldo(jogo.GetPreco())
        if transacao == True:
            self.AdicionarJogoBiblioteca(jogo, remetente)

    def realizarCompra(self, titulo, idComprador, idRemetente = None):
        if idRemetente == None:
            idRemetente = idComprador
        if self.buscarJogo(titulo) != None and self.buscarId(idComprador) != None and self.buscarId(idRemetente) != None:
            comprador =  self.buscarId(idComprador)
            remetente = self.buscarId(idRemetente)
            jogo = self.buscarJogo(titulo)
            if jogo in remetente.getBiblioteca():
                print("Ja possui o jogo")
            else:
              self.ComprarJogo(jogo, comprador, remetente)
        else:
            if self.buscarJogo(titulo) == None:
                print("Jogo não encontrado")
            if self.buscarId(idComprador) == None:
                print("Comprador não encontrado")
            if self.buscarId(idRemetente) == None:
                print("Remetente não encontrado")
