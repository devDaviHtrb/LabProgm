#Crie uma classe chamada "livro" com os seguintes atributos: título, autor, número de paginas. método detalhes e ele vai imprimir todos os atributos do livro.
#crie uma lista de objetos do tipo livro e imprima os detalhes de cada um deles.
#classe chamada "produto" atributos: nome, preço, quantidade. 2 métodos: calcular valor total (preço * quantidade), atualizar quantidade (atualizar a quantidade de produtos, recebendo um novo valor). Crie alguns objetos do tipo "produto" calcule seus valores totais e atualize a quantidade de cada um deles.
#crie uma classe que simule um carrinho de compra de um e-commerce
class Livro:
    def __init__(self, NumeroDePaginas, autor, titulo ):
        self._titulo = titulo
        self._autor = autor 
        self._NumeroDePaginas = NumeroDePaginas
    def Detalhes(self):
        print(f"Titulo:{self._titulo}\n Autor:{self._autor}\n Numero de paginas: {self._NumeroDePaginas}")

livros = [ Livro(12, "klebinho", "Crepusculo"), Livro(13, "klebinho", "Crepusculo 2"), Livro(12, "klebinho", "Crepusculo 3")]

for livro in livros:
    livro.Detalhes()


