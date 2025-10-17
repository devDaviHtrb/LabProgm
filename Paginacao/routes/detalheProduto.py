from flask import Blueprint, render_template
from models.produtos import PRODUTOS

detalhesProdutos = Blueprint("detalhesProdutos", __name__)

@detalhesProdutos.route("/detalhe_produto/<produto_id>")
def detalhe(produto_id):
    return render_template("detalhe.html", product = PRODUTOS[int(produto_id)-1])