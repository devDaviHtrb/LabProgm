from flask import *
from routes.sessao import *
noticias = [{"categoria":"Política", "titulo":"Noticia 1", "data":"10 de Julho de 2024"},{"categoria":"Política", "titulo":"Noticia 2", "data":"10 de Julho de 2024"},{"categoria":"Política", "titulo":"Noticia 3", "data":"10 de Julho de 2024"},{"categoria":"Esportes","titulo":"Noticia 1","data":"10 de Julho de 2024"},{"categoria":"Esportes","titulo":"Noticia 2","data":"10 de Julho de 2024"},{"categoria":"Esportes","titulo":"Noticia 3","data":"10 de Julho de 2024"},{"categoria":"Lazer","titulo":"Noticia 1","data":"10 de Julho de 2024"},{"categoria":"Lazer","titulo":"Noticia 2","data":"10 de Julho de 2024"},{"categoria":"Lazer","titulo":"Noticia 3","data":"10 de Julho de 2024"}]
home = Blueprint("home", __name__)

@home.route("/home", methods={"GET", "POST"})
def Home():
    session["PagAnterior"] = request.endpoint
    username = request.cookies.get("username")
    filtro = request.cookies.get("filtro")
    mode = request.cookies.get("mode")
    print(filtro)
    if not username:
        return redirect(url_for("login"))
    if not mode:
        mode = "0"
    return render_template("Home.html", mode=int(mode), username=username, filtro=filtro, noticias=noticias)