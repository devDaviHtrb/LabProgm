from flask import *
import secrets

from routes.BatalhaNaval import batalhanaval
from routes.AdivinheOnumero import adivinheOnumero
from routes.Quizz import quizz
from routes.Home import home
from routes.JogoDaForca import forca

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
 


app.register_blueprint(home)
app.register_blueprint(batalhanaval)
app.register_blueprint(adivinheOnumero)
app.register_blueprint(quizz)
app.register_blueprint(forca)

        



@app.route('/PedraPapelTesoura',methods=["GET", "POST"])
def PedraPapelTesoura():
    return render_template("PedraPapelTesoura.html")
@app.route('/Hanoi',methods=["GET", "POST"])
def Hanoi():
    return render_template("Hanoi.html")






if __name__ == "__main__":
    app.run(debug=True)