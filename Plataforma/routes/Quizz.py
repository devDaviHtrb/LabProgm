from flask import *
from Classes import BancodePerguntas, Pergunta

Db = BancodePerguntas()
pergunta = Pergunta("O Flask é um framework javascript", True)
Db.adicionaPergunta(pergunta)
Db.adicionaPergunta(pergunta)
def IniciarSessao():
    session["FimJogo"] = False
    session["acertos"] = 0
    session["erros"] = 0
    session["resposta"] = None
    session["IndicePergunta"] = 0
quizz = Blueprint("Quizz", __name__)
@quizz.route("/Quizz", methods=["GET", "POST"])
def Quizz():
    if "resposta" not in session or request.form.get("NovoJogo"):
        IniciarSessao()
        return redirect(url_for("Quizz")) #direciona para o metodo get
        

    if request.method == "POST" and not session.get('FimJogo'):

        if "verdadeiro" in request.form:
            session["resposta"] = True
            print("funciona")
        else:
            session["resposta"] = False
        if session["resposta"]== Db.banco[0].resposta:
            session["acertos"]+=1 
        else:
            session["erros"]=+ 1
        if  session["IndicePergunta"] + 1  < len(Db.banco):
            session["IndicePergunta"] += 1
            return render_template("Quizz.html", erros = session["erros"], acertos=session["acertos"], pergunta=Db.banco[session["IndicePergunta"]].titulo )
        else:
             session["FimJogo"] = True
             return render_template("Quizz.html", erros = session["erros"], acertos=session["acertos"], pergunta="Parabéns você finalizou o quizz!!!", fim=session['FimJogo'] )
        
    return render_template("Quizz.html", erros = session["erros"], acertos=session["acertos"],  pergunta=Db.banco[session["IndicePergunta"]].titulo, fim=session['FimJogo'])

