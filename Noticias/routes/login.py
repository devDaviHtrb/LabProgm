from flask import *
from routes.sessao import *

USER_CONST = "admin"
PASSWORD_USER = "123"

login = Blueprint("login", __name__)

@login.route("/login", methods=["GET", "POST"])
def Login():
    message = ""
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        if user == "admin" and password == "123":
            response = make_response(redirect(url_for("profile.Profile")))
            response.set_cookie("username", user) #MAX_AGE é em segundos: 10min
            response.set_cookie("mode", "0", max_age=30*60)
            response.set_cookie("filtro", "Todas")
            sessao()
            session["PagAnterior"] = request.endpoint
            return response
        else:
            message = "The user or password provided is incorrect. Try again"
    
    return render_template('login.html', error=message)