from flask import *
import secrets

from routes.BatalhaNaval import batalhanaval
from routes.AdivinheOnumero import adivinheOnumero
from routes.Quizz import quizz
from routes.Home import home
from routes.JogoDaForca import forca
from routes.PedraPapelTesoura import PedraPapelTesoura
from routes.Hanoi import Hanoi

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
 
app.register_blueprint(home)
app.register_blueprint(batalhanaval)
app.register_blueprint(adivinheOnumero)
app.register_blueprint(quizz)
app.register_blueprint(forca)
app.register_blueprint(PedraPapelTesoura)
app.register_blueprint(Hanoi)  

if __name__ == "__main__":
    app.run(debug=True)