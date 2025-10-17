from flask import Blueprint, redirect, request, url_for

from models.produtos import PRODUTOS

deleteProduto = Blueprint("deleteProduto", __name__)

@deleteProduto.route("/deleteProduto", methods=["POST"])
def DeleteProduto():
    if request.method == "POST":
        nome = request.form["nome"]
        for produto in PRODUTOS:
            if produto["nome"] == nome:
                del PRODUTOS[PRODUTOS.index(produto)]

        return redirect(url_for("insertProdutoPagina.listar_produtos"))