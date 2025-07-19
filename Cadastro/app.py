from flask import *
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return redirect(url_for('registrarUsuario'))
@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        flash(f'Usuário {username} cadastrado com sucesso!', 'success')
        response = make_response(redirect(url_for("register")))
        response.set_cookie("username", username, max_age=10*60)
        response.set_cookie("password", password,  max_age=10*60)
        response.set_cookie("email", email,  max_age=10*60)
        return response
    return render_template("formulario.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    print(request.cookies.get("username"))
    return render_template("formulario.html")

if __name__ == ("__main__"):
    app.run(debug=True)
