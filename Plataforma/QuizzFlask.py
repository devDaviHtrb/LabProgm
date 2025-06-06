from flask import *
import random
import secrets

class Pergunta:
    def __init__(self, titulo, resposta):
        self.titulo = titulo

        self.resposta = resposta
        
class BancodePerguntas:
    def __init__(self, banco=[]):
        self.banco = banco

    def adicionaPergunta(self, pergunta):
        self.banco.append(pergunta)
Db = BancodePerguntas()
pergunta = Pergunta("O Flask é um framework javascript", True)
Db.adicionaPergunta(pergunta)
Db.adicionaPergunta(pergunta)
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def IniciarSessao():
    session["acertos"] = 0
    session["erros"] = 0
    session["resposta"] = None
    session["FimJogo"] = False
    session["IndicePergunta"] = 0


@app.route("/Quizz", methods=["POST", "GET"])
def Quizz():
    if "resposta" not in session:
        IniciarSessao()
    
    if request.method == "GET" and not session.get('FimJogo'):
        verdadeiro = request.form["verdadeiro"]
        if verdadeiro:
            session["resposta"] = True
            print(verdadeiro)
        else:
            session["resposta"] = False
        if session["resposta"]== Db.banco[0].resposta:
            session["acertos"]+=1 
        else:
            session["erros"]=+ 1
        session["IndicePergunta"] += 1
       
        return render_template("Quizz.html", erros = session["erros"], acertos=session["acertos"], pergunta=Db.banco[session["IndicePergunta"]].titulo )
        
    return render_template("Quizz.html", erros = session["erros"], acertos=session["acertos"],  pergunta=Db.banco[session["IndicePergunta"]].titulo)



   



if __name__ == "__main__":
    app.run(debug=True)