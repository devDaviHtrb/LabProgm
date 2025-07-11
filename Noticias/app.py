
from flask import *
import secrets

from routes.home import home
from routes.login import login
from routes.logout import logout
from routes.filtro import filtro
from routes.mode import mode
from routes.profile import profile
from routes.cadastro import cadastro

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)



app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(profile)
app.register_blueprint(mode)
app.register_blueprint(filtro)
app.register_blueprint(cadastro)

@app.route("/", methods=["GET", "POST"])
def Default():
    return redirect(url_for("home.Home"))




if __name__ =="__main__":
    app.run(debug=True)
