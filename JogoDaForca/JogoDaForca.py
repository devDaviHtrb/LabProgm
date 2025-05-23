from palavra import Palavra
from Db import BancodePerguntas
class Jogo:
    def __init__(self, banco):
        self.banco = banco

    def Jogar(self):
        for n in self.banco:
            vida = 6
            letras = []
            letrasDapalavra = list(n)
            while vida!=0:

                letrasAcertadas = []
                for h in letrasDapalavra:
                    letrasAcertadas.append("")
                print(letrasAcertadas)

                letraChute = input("Digite uma letra: ").lower()
                
                if letraChute in letrasDapalavra:
                    letras.append(letraChute)
                    contador = 0
                    for indice, elemento in enumerate(letrasDapalavra):
                        if elemento == letraChute:
                            letrasAcertadas.splice(indice, 0, letraChute)

                    for i in letrasDapalavra:
                        if i in letras:
                            contador +=1
                            letrasAcertadas.splice(letraChute.index())
                    if contador == len(letrasDapalavra):
                        return
                else:
                    vida -= 1

palavra1 = Palavra("casa")
Db = BancodePerguntas()
Db.adicionaPergunta(palavra1.palavra)
jogo = Jogo(Db.banco)
jogo.Jogar()
