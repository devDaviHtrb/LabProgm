from flask import *

filtro = Blueprint("filtro", __name__)

@filtro.route("/filtro", methods=["GET", "POST"])
def Filtro():
    if request.method=="POST":
        response = make_response(redirect(url_for("home.Home")))
        filtroValor = request.form["filtro"]
        response.set_cookie("filtro", filtroValor)
    return response