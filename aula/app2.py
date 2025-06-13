from flask import *

app = Flask(__name__)

@app.route("/")

def home():
    produtos = ["maça", "banana", "larranja"]

    logado = True

    return render_template("home.html", produtos=produtos,logado=logado)