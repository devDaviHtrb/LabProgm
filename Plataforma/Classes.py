class Pergunta:
    def __init__(self, titulo, resposta):
        self.titulo = titulo

        self.resposta = resposta
        
class BancodePerguntas:
    def __init__(self, banco=[]):
        self.banco = banco

    def adicionaPergunta(self, pergunta):
        self.banco.append(pergunta)