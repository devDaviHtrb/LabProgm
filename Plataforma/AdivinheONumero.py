from flask import Flask, render_template, request, session, redirect, url_for
import random
import secrets
import random
class Navio:
    def __init__(self,  linha, coluna, orientacao, tamanho):
        self.linha = linha
        self.coluna = coluna
        self.orientacao = orientacao
        self.tamanho = tamanho
class Tabuleiro:
    def __init__(self):
        self.campo = [[0 for coluna in range(0, 10)] for linha in range(0,10)]
        self.navioslista = []


    def adicionaNavio(self, quantidade):
        navios = 0
        while navios < quantidade:
            linha = random.randint(0,9)
            coluna= random.randint(0,9)
            orientacao =random.randint(0,1)
            tamanho = random.randint(0,3)
            navio = 0
            if len(self.navioslista)>0:
                while self.navioslista[navio].linha == linha and self.navioslista[navio].coluna == coluna and orientacao == self.navioslista[0].orientacao:
                    linha = random.randint(0,9)
                    coluna= random.randint(0,9)
                    orientacao =random.randint(0,1)
                    tamanho = random.randint(0,3)
            if 10-linha>tamanho and orientacao == 0:#Horizontal
                for n in range(0, tamanho):
                    try:
                        self.campo[linha][coluna+n-1] = 1
                        self.navioslista.append(Navio(linha, coluna, orientacao, tamanho))
                    except ValueError:
                        navios = navios
                navios+=1
            if 10-coluna>tamanho and orientacao == 1:#Horizontal
                for n in range(0, tamanho):
                    try:
                        self.campo[linha+n-1][coluna] = 1
                        self.navioslista.append(Navio(linha, coluna, orientacao, tamanho))
                    except ValueError:
                        navio = navio
                navios+=1
            navio+=1
                
    def Atira(self, x, y):
        if x<=10 and y<=10:
            if self.campo[y-1][x-1] == 1:
                self.campo[y-1][x-1] = 2
                return print("Navio acertado")
            else:
                return print("Água acertada")
        else:
            print("Jogada invalida")



app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# --- Lógica do Jogo Adivinhar o Número ---
def sessao():
    tabuleiro = Tabuleiro()
    tabuleiro.adicionaNavio(5)
    session["tabuleiro"] = tabuleiro.campo
    session["buttons"] = [f'casa{n+1}' for n in range(0, 110)]
    session["FimJogo"] =False

@app.route('/batalhaNaval',methods=["GET", "POST"])
def batalhaNaval():
    if "tabuleiro" not in session or request.form.get("NovoTabuleiro"):
        sessao()
        return render_template("BtNaval.html", tabuleiro=session["tabuleiro"], op=0)
    if request.method == "POST" and not session.get('FimJogo'):
        
        for button in session["buttons"]:
            if button in request.form:
                try:
                    index = int(session["buttons"].index(button))
                    if int(request.form[button])== 0:
                       
                        print(session["tabuleiro"][9])
                        if index>=100:
                            session["tabuleiro"][9][session["buttons"].index(button)-100] = "X"
                            print(session["buttons"].index(button))
                        else:
                             session["tabuleiro"][int(str(index)[0])-1][session["buttons"].index(button)-10*int(str(index)[0])] = "X" 
                    if int(request.form[button])== 1:
                        
                        if index>100:
                            print(session["buttons"].index(button))
                            session["tabuleiro"][9][session["buttons"].index(button)-100] = "O"
                        else:
                            session["tabuleiro"][int(str(index)[0])-1][session["buttons"].index(button)-10*int(str(index)[0])] = "O"
                        print(session["tabuleiro"])
                      
                        uns = 0
                        for x in session["tabuleiro"]:
                            uns+= x.count(1)
                        if uns==0:
                            session["FimJogo"]=True
                        
                    session.modified =True
                except ValueError:
                    return render_template("BtNaval.html", tabuleiro=session["tabuleiro"], fimJogo=session["FimJogo"])
                
                
    return render_template("BtNaval.html", tabuleiro=session["tabuleiro"], fimJogo=session["FimJogo"])

if __name__ == "__main__":
    app.run(debug=True)
   
