from flask import *
from routes.sessao import *
import json



login = Blueprint("login", __name__)

@login.route("/login", methods=["GET", "POST"])
def Login():
    message = ""
    if request.method == "POST":
        DB = 'USERS.json'

        try:
            with open(DB, 'r') as f:
                USERS = json.load(f)
        except FileNotFoundError:
            USERS = {} 
        user = request.form["username"]
        password = request.form["password"]
        for key in list(USERS.keys()):
            if USERS[key]["USERNAME"] == user and USERS[key]["PASSWORD"] == password:
                response = make_response(redirect(url_for("profile.Profile")))
                response.set_cookie("username", user) #MAX_AGE é em segundos: 10min
                response.set_cookie("mode", "0", max_age=30*60)
                response.set_cookie("filtro", "Todas")
                sessao()
                session["PagAnterior"] = request.endpoint
                return response
        if "visitas" not in session:
            message = "The user or password provided is incorrect. Try again"
    
    return render_template('login.html', error=message)