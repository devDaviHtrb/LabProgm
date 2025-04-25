class Carrinho:
    def __init__(self, quantidadeDeProdutos=0):
        self._QuantidadeProdutos = quantidadeDeProdutos

    def AdicionaItem(self):
        self._QuantidadeProdutos += 1

    def RemoveItem(self):
        if self.VerificaCarrinho() != "Vazio":
            self._QuantidadeProdutos -= 1
        else:
            print("Seu carrinho está vazio")

    def VerificaCarrinho(self):
        if self._QuantidadeProdutos == 0:
            return "Vazio"
    
    def Comprar(self):
        self.comprando = True
        while self.comprando==True:
            operacao = int(input("Digite 1 para adicionar e 2 para remover produtos: ")) 
            while operacao != 1 or operacao!=2:
                if operacao == 1:
                    self.AdicionaItem()
                    break
                elif operacao == 2:
                    self.RemoveItem()
                    break
                else:
                    print("Operação Invalida")
                    operacao = int(input("Digite 1 para adicionar e 2 para remover produtos: ")) 
            verProduto = input("Deseja ver a quantidade de produtos: S/N").upper()
            if verProduto1 == "S":
                print(f"{self._QuantidadeProdutos}")
            else:
                print("Ok")
            if input("Deseja continuar no carrinho: S/N").upper() == "N":
                self.comprando = False
carrinho = Carrinho()
carrinho.Comprar()