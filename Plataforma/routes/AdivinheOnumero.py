import random
from flask import *

def IniciarSessao():
    session["FimJogo"] = False
    session['numero_secreto_an'] = random.randint(0, 100)
    session['tentativas_an'] = 0
    session['mensagem_an'] = f"Adivinhe um número entre 0 e 100."
    session['ultimo_palpite_an'] = None # Para mostrar o último palpite

        
adivinheOnumero = Blueprint("adivinheOnumero", __name__)
@adivinheOnumero.route('/adivinhar_numero', methods=['GET', 'POST'])
def adivinhar_numero():
    """Rota principal para o jogo Adivinhar o Número."""
    if 'numero_secreto_an' not in session or request.form.get('novo_jogo_an'):
        IniciarSessao()
        if request.form.get('novo_jogo_an'):
            return redirect(url_for('adivinheOnumero.adivinhar_numero')) # Redireciona para limpar o POST

    if request.method == 'POST' and not session.get('FimJogo'):
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
                    session['FimJogo'] = True
                
            except ValueError:
                session['mensagem_an'] = "Entrada inválida. Por favor, insira um número inteiro."
                session['ultimo_palpite_an'] = request.form.get('palpite_usuario', '') # Mantém o valor inválido para mostrar
            
            session.modified = True
            return redirect(url_for('adivinheOnumero.adivinhar_numero')) # Redireciona para GET

    return render_template('AdivinheOnumero.html',
                           mensagem=session.get('mensagem_an'),
                           jogo_terminado=session.get('FimJogo', False),
                           tentativas=session.get('tentativas_an', 0),
                           limite_inferior=0,
                           limite_superior=100,
                           ultimo_palpite=session.get('ultimo_palpite_an'))