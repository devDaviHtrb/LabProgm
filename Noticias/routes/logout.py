from flask import *

logout = Blueprint("logout", __name__)

@logout.route("/logout")
def Logout():
    response = make_response(redirect(url_for("login.Login")))
    response.set_cookie("username", '', expires=0) #expire mata o cookie
    return response
