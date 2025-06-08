import random
from  flask import *
import secrets
from Classes import *
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

Db = BancodePerguntas()
pergunta = Pergunta("O Flask é um framework javascript", True)
Db.adicionaPergunta(pergunta)
Db.adicionaPergunta(pergunta)

@app.route("/", methods=["POST", "GET"])
def Home():
    return render_template("Home.html")


def IniciarSessao():
    if request.path == "/Quizz":
        session["acertos"] = 0
        session["erros"] = 0
        session["resposta"] = None
        session["FimJogo"] = False
        session["IndicePergunta"] = 0
    if request.path == "/adivinhar_numero":
        session['numero_secreto_an'] = random.randint(0, 100)
        session['tentativas_an'] = 0
        session['mensagem_an'] = f"Adivinhe um número entre 0 e 100."
        session['jogo_an_terminado'] = False
        session['ultimo_palpite_an'] = None # Para mostrar o último palpite

@app.route("/Quizz", methods=["GET", "POST"])
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

@app.route('/adivinhar_numero', methods=['GET', 'POST'])
def adivinhar_numero():
    """Rota principal para o jogo Adivinhar o Número."""
    if 'numero_secreto_an' not in session or request.form.get('novo_jogo_an'):
        IniciarSessao()
        if request.form.get('novo_jogo_an'):
            return redirect(url_for('adivinhar_numero')) # Redireciona para limpar o POST

    if request.method == 'POST' and not session.get('jogo_an_terminado'):
        if 'number' in request.form:
            try:
                palpite = int(request.form['number'])
                session['ultimo_palpite_an'] = palpite
                session['tentativas_an'] += 1
                
                numero_secreto = session.get('numero_secreto_an')

                if palpite < 0 or palpite > 100:
                    session['mensagem_an'] = f"Por favor, insira um número entre {0} e {100}."
                elif palpite < numero_secreto:
                    session['mensagem_an'] = f"O número {palpite} é muito baixo. Tente um maior!"
                elif palpite > numero_secreto:
                    session['mensagem_an'] = f"O número {palpite} é muito alto. Tente um menor!"
                else: # Acertou!
                    session['mensagem_an'] = f"Parabéns! Você acertou o número {numero_secreto} em {session['tentativas_an']} tentativa(s)!"
                    session['jogo_an_terminado'] = True
                
            except ValueError:
                session['mensagem_an'] = "Entrada inválida. Por favor, insira um número inteiro."
                session['ultimo_palpite_an'] = request.form.get('palpite_usuario', '') # Mantém o valor inválido para mostrar
            
            session.modified = True
            return redirect(url_for('adivinhar_numero')) # Redireciona para GET

    return render_template('AdivinheOnumero.html',
                           mensagem=session.get('mensagem_an'),
                           jogo_terminado=session.get('jogo_an_terminado', False),
                           tentativas=session.get('tentativas_an', 0),
                           limite_inferior=0,
                           limite_superior=100,
                           ultimo_palpite=session.get('ultimo_palpite_an'))

@app.route('/PedraPapelTesoura',methods=["GET", "POST"])
def PedraPapelTesoura():
    return render_template("PedraPapelTesoura.html")
@app.route('/Hanoi',methods=["GET", "POST"])
def Hanoi():
    return render_template("Hanoi.html")
@app.route('/Forca', methods=["GET", "POST"])
def Forca():
    return render_template("Forca.html")
@app.route('/batalhaNaval',methods=["GET", "POST"])
def batalhaNaval():
    return render_template("BtNaval.html")



if __name__ == "__main__":
    app.run(debug=True)