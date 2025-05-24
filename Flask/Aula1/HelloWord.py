from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/enviar', methods=["post"])
def enviar():
    nome = request.form["nome"]
    cidade = request.form["cidade"]

    return render_template("Validation.html", nome = nome, cidade = cidade)
if __name__ == "__main__":
    app.run(debug=True)