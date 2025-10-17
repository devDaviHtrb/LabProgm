from flask import Blueprint, render_template
from models.produtos import PRODUTOS

insertProdutopagina = Blueprint("insertProdutoPagina", __name__)

@insertProdutopagina.route("/insertProdutoPagina", methods=["POST", "GET"])
def listar_produtos():
    return render_template("inserirDeletar.html")