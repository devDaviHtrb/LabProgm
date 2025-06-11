from flask import *

Hanoi = Blueprint("Henoi", __name__)

@Hanoi.route("/Hanoi", methods=["GET", "POST"])
def hanoi():
    return render_template("Hanoi.html")