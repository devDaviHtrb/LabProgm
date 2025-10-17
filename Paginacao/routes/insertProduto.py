from flask import Blueprint, redirect, render_template, request, url_for
from models.produtos import PRODUTOS

insertProduto = Blueprint("insertProduto", __name__)

@insertProduto.route("/insertProduto", methods=["POST", "GET"])
def inserirProduto():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        PRODUTOS.append({"id":len(PRODUTOS)+1, "nome":nome, "preco":float(preco)})

    return redirect(url_for("insertProdutoPagina.listar_produtos"))