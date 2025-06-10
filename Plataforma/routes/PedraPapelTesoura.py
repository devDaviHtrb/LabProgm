from secrets import randbelow

class Game:
    def __init__(self):
        self.Options = ["Paper", "scissor", "rock"]
        self.Continue()

    def Play(self, computer):

        computer = computer
        print(computer)
        gamer = input("Choose an option:Paper, scissor, rock ").lower()
       
        if gamer =="paper" and computer == "rock" or gamer =="rock" and computer == "scissor" or gamer =="scissor" and computer == "paper":
            print("Gamer's win")
            return
        elif gamer == computer:
            print("Tie")
            return
        else:
            print("Computer's win")
            return

    def Continue(self):
        if input("Do you want to play? Y/N").upper() == "Y":
            self.Play(self.Options[randbelow(2)])
            return self.Continue()
        else:
            return
        
jogo = Game()