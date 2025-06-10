from flask import *
from Classes import BancodePerguntas
import random
forca = Blueprint("Forca", __name__)

def IniciaSessao():
    palavra1 = "casa"
    palavra2 = "casebre"
    Db = BancodePerguntas()
    Db.adicionaPergunta(palavra1)
    Db.adicionaPergunta(palavra2)
    session["FimJogo"] = False
    session["Palavra"] = Db.banco[random.randint(0, len(Db.banco)-1)]
    session["Letras"] = list(session["Palavra"])
    session["LetrasAcertadas"] = []
    session["LetrasErradas"] = []
    session["LetraChute"] = None
    session["vida"] = 6

@forca.route("/forca", methods=["GET", "POST"])
def Forca():
    if "Palavra" not in session or request.form.get("NovoJogo"):
        IniciaSessao()
        return redirect(url_for("Forca.Forca"))
    if request.method == "POST" and not session.get("FimJogo"):

        if "adivinhar" in request.form:
            letra = request.form.get("letra")
            if len(list(letra))==1:
                if  letra in session["Letras"] and letra not in session["LetrasAcertadas"]:
                    session["LetrasAcertadas"].append(letra)
                    session["LetrasAcertadas"].sort()
                    session["FimJogo"]=True
                    for letra in session["Letras"]:
                        if letra not in session["LetrasAcertadas"]:
                            session["FimJogo"]=False
                else:
                    if letra not in session["LetrasErradas"]:
                        session["LetrasErradas"].append(letra)
                        session["LetrasErradas"].sort()
                        session["vida"]-=1
                        if session["vida"]<1:
                            session["FimJogo"]=True
                session.modified = True
            
        return render_template("Forca.html", letras=session["Letras"], acertos=session["LetrasAcertadas"], vida=session["vida"], erros=session["LetrasErradas"], FimJogo= session["FimJogo"])
    return render_template("Forca.html", letras=session["Letras"], acertos=session["LetrasAcertadas"], erros=session["LetrasErradas"], vida=session["vida"], FimJogo= session["FimJogo"])


