from flask import *
from Classes import Peca
from Classes import torre
import pickle
Hanoi = Blueprint("Hanoi", __name__)




def IniciarSessao():
    
    session["FimJogo"] = False
    session["TorreAtual"] = None
    session["TorreAlvo"] = None
    session["Torres"] = [["peca1", "peca2", "peca3", "peca4", "peca5"], [], []]

@Hanoi.route("/Hanoi", methods=["GET", "POST"])
def hanoi():

    if "TorreAtual" not in session or request.form.get("NovoJogo"):
        IniciarSessao()
        return redirect(url_for("Hanoi.hanoi"))
    
    if request.method=="POST" and not session["FimJogo"]:
        if session["TorreAtual"] ==None:
            if "torre1" in request.form:
                session["TorreAtual"] = session["Torres"][0]
            elif "torre2" in request.form:
                session["TorreAtual"] = session["Torres"][1]
            elif "torre3" in request.form:
                session["TorreAtual"] = session["Torres"][2]
        else:
            if "torre1" in request.form:
                session["TorreAlvo"] = session["Torres"][0]
            elif "torre2" in request.form:
                session["TorreAlvo"] = session["Torres"][1]
            elif "torre3" in request.form:
                session["TorreAlvo"] = session["Torres"][2]
                print("torre 3")
            session.modified = True
            if len(session["TorreAlvo"]) > 0:
                if int(session["TorreAtual"][len(session["TorreAtual"])-1][4]) > int(session["TorreAlvo"][len(session["TorreAlvo"])-1][4]) :
                    session["Torres"][session["Torres"].index(session["TorreAlvo"])].append(session["Torres"][session["Torres"].index(session["TorreAtual"])].pop())
            else:
                if "torre2" in request.form:
                    session["Torres"][1].append(session["Torres"][session["Torres"].index(session["TorreAtual"])].pop())
                elif "torre3" in request.form:
                    session["Torres"][2].append(session["Torres"][session["Torres"].index(session["TorreAtual"])].pop())
                else:
                    session["Torres"][0].append(session["Torres"][session["Torres"].index(session["TorreAtual"])].pop())
            session["TorreAlvo"] = None
            session["TorreAtual"] = None
            if len(session["Torres"][2]) ==5:
                session["FimJogo"] = True
        session.modified = True
    return render_template("Hanoi.html", torres = session["Torres"], FimJogo = session["FimJogo"])
