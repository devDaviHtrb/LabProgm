 
from Db import BancodePerguntas
class Jogo:
    def __init__(self, banco):
        self.banco = banco
        self.Jogar()

    def Jogar(self):
        for n in self.banco:
            vida = 6
            letrasDapalavra = list(n)
            letrasAcertadas = ["" for vazio in range(0, len(letrasDapalavra))]
            contador = 0

            while vida!=0:
                print(letrasAcertadas)

                letraChute = input("Digite uma letra: ").lower()
                
                if letraChute in letrasDapalavra:
                    for g in range(0,len(letrasDapalavra)):
                        if letraChute == letrasDapalavra[g]:
                            contador +=1
                            letrasAcertadas[g] = letraChute          
                    if contador == len(letrasDapalavra): break
                else:
                    vida -= 1
            print(f"A palavra correta é {n}")
            print("Você acertou") if vida>0 else print("Você perdeu")
            if input("Deseja Continuar jogando S/N?").upper() == "N": return 

palavra1 = "casa"
palavra2 = "casebre"
Db = BancodePerguntas()
Db.adicionaPergunta(palavra1)
Db.adicionaPergunta(palavra2)
jogo = Jogo(Db.banco)
