from flask import Flask, render_template, request, redirect, url_for, session
from models import UsuarioModel

app = Flask(__name__)
user_model = UsuarioModel()
app.secret_key ="sdfsdf"

@app.route("/usuarios")
def listar_usuarios():
    if session.get("admin")== "comum":
        return redirect(url_for("bem_vindo"))
    users = user_model.get_all()
    return render_template("user.html", lista_de_usuarios=users)

@app.route("/Usuarios/novo", methods=["POST"])
def adicionar_usuario():
    nome = request.form["nome"]
    email = request.form["email"]
    password = request.form["password"]
    user_type =True if  request.form["user_type"] else False
    user_model.save(nome, email, password, user_type)
    return redirect(url_for("listar_usuarios"))

@app.route("/Usuarios/deletar/<id>")
def deletar_usuario(id):
    user_model.delete(id)
    return redirect(url_for("listar_usuarios"))

@app.route("/Usuarios/login", methods=["POST"])
def logar():
    session["user"] = request.form["username"]
    session["admin"] = user_model.isAdmin(request.form["username"])
    if session.get("admin")== "comum":
        print( session.get("admin"))
        return redirect(url_for("bem_vindo"))
    else:
        print( session.get("admin"))
        return redirect(url_for("listar_usuarios"))

@app.route("/")
def bem_vindo():
    return render_template("Welcome.html")

if __name__ == "__main__":
    app.run(debug=True)   