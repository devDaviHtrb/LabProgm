from flask import Blueprint, request, jsonify
from models.produtos import PRODUTOS

buscarProduto = Blueprint("buscarProduto", __name__)

@buscarProduto.route("/api/buscar_produto/<dados>")
def busca(dados):
    nome_produto = dados

    resultado = [p for p in PRODUTOS if nome_produto.lower() == p["nome"].lower()]
    print(resultado)
    return jsonify({"produtos":resultado})
