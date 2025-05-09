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
            if jogador.getId == id:
                return jogador
        return None
    
    def listarCatalogo(self):
        for jogo in self.__catalogoJogos:
            jogo.exibirDetalhes()

    def AdicionarJogoBiblioteca(self, jogo, jogador):
        return jogador.__bibliotecaJogos.append(jogo)

    def ComprarJogo(self, jogo, jogador):
        if jogador.DebitaSaldo(jogo.GetPreco()) == True:
            self.AdicionarJogoBiblioteca(jogo, jogador)

    def realizarCompra(self, titulo, id):
        if self.buscarJogo(titulo) != None and self.buscarId(id) != None:
            jogador =  self.buscarId(id)
            jogo = self.buscarJogo(titulo)
            if jogo in jogador.__bibliotecaJogos:
                print("Ja possui o jogo")
            else:
              self.ComprarJogo(jogo, jogador)
        else:
            if self.buscarJogo(titulo) == None:
                print("Jogo não encontrado")
            if self.buscarId(id) == None:
                print("Jogador não encontrado")
