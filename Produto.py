class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_produtos(self):
        print(f"Produto -- {self.nome}\nPreço -- R$ {self.preco:.2f}\nQuantidade -- {self.quantidade}")
        print("-" *45)
