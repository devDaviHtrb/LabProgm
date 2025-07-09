from flask import *
from routes.sessao import *
profile = Blueprint("profile", __name__)

@profile.route("/profile", methods=["GET","POST"])
def Profile():
    if "visitas" not in session and request.cookies.get("username"):
        sessao()
    if session["PagAnterior"] != request.endpoint:
        session["visitas"]+=1
        session["PagAnterior"] = request.endpoint
    mode = request.cookies.get("mode")
    if not mode:
        mode = 0
    session.modified = True
    return render_template("profile.html", username=request.cookies.get("username"), visitas=session["visitas"], mode=int(mode))