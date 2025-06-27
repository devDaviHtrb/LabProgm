from flask import *
import secrets

senha = 12345

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def sessao():
    session["username"] = None
    session["erro"] = False

@app.route("/")
def home():
    produtos = ["maça", "banana", "larranja"]
    
    if "username" not in  session:
        sessao()
    if session["username"]!=None:
        logado = True
    else:
        logado = False
    return render_template("home.html", produtos=produtos,logado=logado, username=session["username"] )
@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", user=username)
@app.route("/loginPage/", methods=["GET", "POST"])
def loginPage():
    return render_template("login.html", erro=session["erro"])

@app.route("/login", methods=["POST"])
def login():   
    if senha==int(request.form.get("senha")):
        session["erro"] = False
        session["username"] = request.form.get("login")
    else:
        session["erro"] = True
        return redirect(url_for("loginPage"))
    print(request.form.get("senha"))
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("loginPage"))
if __name__ == "__main__":
    app.run(debug=True)
