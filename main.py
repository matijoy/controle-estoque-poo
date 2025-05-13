from Produto import Produto
from ProdutoAlimentício import ProdutoAlimenticio
estoque = []
def cadastrarcomum():
    nome = input("Insira o nome do produto que você deseja cadastrar -- ")
    preco = float(input("Insira o preço do produto -- "))
    quantidade = int(input("Insira a quantidade -- "))
    produto = Produto(nome, preco, quantidade)
    estoque.append(produto)

def cadastroalimenticio():
    nome = input("Insira o nome do produto que você deseja cadastrar -- ")
    preco = float(input("Insira o preço do produto -- "))
    quantidade = int(input("Insira a quantidade -- "))
    data_validade = int(input("Insira a data de validade -- "))
    produtoalim = ProdutoAlimenticio(nome, preco, quantidade, data_validade)
    estoque.append(produtoalim)

def lista():
    print("===PRODUTOS===")
    for produto in estoque:
        produto.exibir_produtos()

def menu():
    opcao = int(input("===MENU ESTOQUE===\n1. Cadastrar produto comum\n2. Cadastrar produto alimentício\n3. Listar todos os produtos\n4. Sair\n"))
    if opcao == 1:
        cadastrarcomum()
        menu()
    if opcao == 2:
        cadastroalimenticio()
        menu()
    if opcao == 3:
        lista()
        menu()
    if opcao < 1 or opcao > 4:
        print("Opção inválida!")
        menu()

 
menu()