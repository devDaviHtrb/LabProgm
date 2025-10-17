from flask import Blueprint, render_template, request
from models.produtos import PRODUTOS

insertProduto = Blueprint("insertProduto", __name__)

@insertProduto.route("/insertProduto", methods=["POST", "GET"])
def listar_produtos():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        PRODUTOS.append({"id":len(PRODUTOS)+1, "nome":nome, "preco":float(preco)})

    return render_template("inserir.html", produtos=PRODUTOS)