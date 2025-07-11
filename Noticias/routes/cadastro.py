from flask import *
import json

cadastro = Blueprint("cadastro", __name__)
DB = 'USERS.json'

try:
    with open(DB, 'r') as f:
        USERS = json.load(f)
except FileNotFoundError:
    USERS = {} 


@cadastro.route("/cadastro", methods=["POST", "GET"])
def Cadastro():
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            USERS[request.form["username"].upper()]={}
            USERS[request.form["username"].upper()]["USERNAME"] = request.form["username"]
            USERS[request.form["username"].upper()]["PASSWORD"] = request.form["password"]
            with open(DB, 'w') as f:
                json.dump(USERS, f, indent=4) 
            return redirect(url_for("login.Login"))
    return render_template("Cadastro.html")