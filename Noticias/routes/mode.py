from flask import *

mode = Blueprint("mode", __name__)

@mode.route("/mode", methods=["GET","POST"])
def Mode():
    response = make_response(redirect(url_for("profile.Profile")))
    if request.method=="POST":
        if request.cookies.get("mode") == "0":
            response.set_cookie("mode","1", max_age=30*60)
        else:
            response.set_cookie("mode", "0", max_age=30*60)
        return response