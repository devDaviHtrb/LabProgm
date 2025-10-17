from flask import Flask
from routes import *
from setup.error import register_handlers

app = Flask(__name__)
app.register_blueprint(produtos)
app.register_blueprint(produtosPaginados)
app.register_blueprint(buscarProduto)
app.register_blueprint(detalhesProdutos)
app.register_blueprint(insertProduto)
app.register_blueprint(deleteProduto)
app.register_blueprint(insertProdutopagina)

register_handlers(app)

if __name__=="__main__":
    app.run(debug=True)