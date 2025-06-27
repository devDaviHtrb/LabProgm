
from flask import *

home = Blueprint("Home", __name__)
@home.route("/", methods=["POST", "GET"])
def Home():
    return render_template("Home.html")

