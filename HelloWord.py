from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Bemvindo/<nome>')
def bemVindo(nome):
    return render_template("BemVindo.html", usuario=nome)
if __name__ == "__main__":
    app.run()