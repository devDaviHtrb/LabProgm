from flask import *
def sessao():
    session["visitas"] = 0
    session["PagAnterior"] = ""