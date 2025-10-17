from flask import Blueprint, render_template
from models.produtos import PRODUTOS

produtos = Blueprint("produtos", __name__)

@produtos.route("/produtos")
def listar_produtos():
    return render_template("produtos.html", produtos=PRODUTOS)