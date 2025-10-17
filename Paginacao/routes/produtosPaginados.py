from flask import Blueprint, jsonify
from models.produtos import PRODUTOS
import math

produtosPaginados = Blueprint("produtosPaginados", __name__)

@produtosPaginados.route("/produtos_paginados")
@produtosPaginados.route("/produtos_paginados/<page>")
def paginar(page=1):
    print(page)
    page = int(page)
    per_page = 5

    start = (page-1)*per_page
    end = start+per_page
    total_pages = math.ceil(len(PRODUTOS) / per_page)


    produtos_da_pagina = PRODUTOS[start:end]

    response = {
        "produtos": produtos_da_pagina,
        "currentPage": page,
        "total_pages": total_pages,
        "has_next": True if page<total_pages else False,
        "has_prev": False if page==1 else True
    }

    return jsonify(response)