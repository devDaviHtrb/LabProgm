from secrets import randbelow
class Game:
    def __init__(self):
        self.Jogar()
        pass

    def Chutar(self):
        self.numero = randbelow(101)
        chute = -1
        while chute != self.numero:
            chute = int(input("Chute um numero entre 0 e 100: "))
            if chute==self.numero:
                print("Você acertou\n")
                return
            elif chute< self.numero:
                print("Chute mais alto\n")
                return
            else:
                print("Chute mais baixo\n")
                return

    def Jogar(self):
        if input("Deseja jogar? S/N").upper() == "S":
            self.Chutar()
            return self.Jogar()
        else:
            return
            
        
jogo = Game()

        