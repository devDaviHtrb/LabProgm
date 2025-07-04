from flask import Flask, render_template, redirect, request, url_for, make_response
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(16)

USER_CONST = "admin"
PASSWORD_USER = "123"


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    color = "blue"
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        if user == USER_CONST and password == PASSWORD_USER:
           
            response = make_response(redirect(url_for("bemvindo")))
            response.set_cookie("username", user, max_age=60*10) #MAX_AGE é em segundos: 10min
            response.set_cookie("color", "blue")
            color = request.cookies.get("color")
            return response
        else:
            message = "The user or password provided is incorrect. Try again"
    
    return render_template('login.html', error=message, color=color)


@app.route('/bemvindo', methods=["POST", "GET"])
def bemvindo():
    username = request.cookies.get("username")
    color = request.cookies.get("color")
    if not username:
        return redirect(url_for("login"))
    if request.method == "POST":
        color = request.form["color"]
        response = make_response(redirect("bemvindo"))
        response.set_cookie("color", color)
        color = request.cookies.get("color")
        print(color)
        return response

    return render_template("bemvindo.html", user=username, color=color)

@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("login")))
    response.set_cookie("username", '', expires=0) #expire mata o cookie
    response.set_cookie("color", "blue",expires=0)
    return response

if __name__ == "__main__":
    app.run(debug=True)