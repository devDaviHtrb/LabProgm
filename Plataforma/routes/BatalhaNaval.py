from flask import *
from Classes import Tabuleiro

def IniciarSessao():
    session["FimJogo"] = False
    
    if request.path== "/batalhaNaval":
        tabuleiro = Tabuleiro()
        tabuleiro.adicionaNavio(5)
        session["tabuleiro"] = tabuleiro.campo
        session["buttons"] = [f'casa{n+1}' for n in range(0, 110)]


batalhanaval= Blueprint("batalha naval", __name__)
@batalhanaval.route('/batalhaNaval',methods=["GET", "POST"])
def batalhaNaval():
    if "tabuleiro" not in session or request.form.get("NovoTabuleiro"):
        IniciarSessao()
        return redirect("batalhaNaval")
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