class Torre:
    def __init__(self, nome, Pecas=None):
        if Pecas != []:
            self.Pecas = Pecas
        self.nome = nome
        self.Pecas = Pecas
        if self.Pecas == None:
            self.Pecas = []