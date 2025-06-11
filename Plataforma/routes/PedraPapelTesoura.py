from secrets import randbelow
from flask import *

        
PedraPapelTesoura = Blueprint("PedraPapelTesoura", __name__)
imgs = ['pedra','papel','tesoura']
def IniciaSessao():
    session["FimJogo"] = False
    session["Jogada"] = None
    session["computador"] = None
    session["mensagem"] = None
@PedraPapelTesoura.route("/PedraPapelTesoura", methods=["GET", "POST"])
def pedraPapelTesoura():
    if "Jogada" not in session or request.form.get("NovoJogo"):
        IniciaSessao()
        return redirect(url_for("PedraPapelTesoura"))
    if request.method=="POST" and not session.get("FimJogo"):
        for img in imgs:
            if img in request.form:
                session["Jogada"] = img
        session["computador"] = imgs[randbelow(2)]
        if session["Jogada"] =="papel" and session["computador"] == "pedra" or session["Jogada"] =="pedra" and session["computador"] == "tesoura" or session["Jogada"] =="tesoura" and session["computador"] == "papel":
            session["mensagem"] = "Você Venceu!!!!"
        elif session["Jogada"] == session["computador"]:
            session["mensagem"] = "Empate!!!"   
        else:
            session["mensagem"] = "Você Perdeu!!!!"
        session["FimJogo"] = True
        session.modified = True
        return redirect(url_for("PedraPapelTesoura"))
    return render_template("PedraPapelTesoura.html", img=session['computador'], mensagem=session["mensagem"], FimJogo=session["FimJogo"])