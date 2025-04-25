class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self._quantidade = quantidade
        self._preco = preco
    
    def ValorTotal(self):
        return self._preco*self._quantidade
    def AtualizarQuantidade(self, Nprodutos):
        self._quantidade = Nprodutos

produtos =[Produto("nome1", 2, 10), Produto("nome2", 3, 10), Produto("nome3", 4, 10)]
n = 1
for produto in produtos:
    n+=4
    print(f"Nome: {produto.nome}; Valor total:{produto.ValorTotal()}")
    produto.AtualizarQuantidade(n)
    print(f"Novo valor total:{produto.ValorTotal()}")