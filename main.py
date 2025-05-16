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
        
def repor():
    if estoque == []:
        print("Você ainda não cadastrou um produto!")
    else:
        pesquisa = input("Insira o nome do produto que você deseja repor -- ")
        for produto in estoque:
            if pesquisa == produto.nome:
                operacao = int(input("Você deseja adicionar quantos itens ao estoque? -- "))
                if operacao < 1:
                    print("Você precisa repor pelo menos uma quantidade de 1 ou maior")
                else:
                    produto.quantidade += operacao
                    print(f"Reposição concluída! Estoque atual -- {produto.quantidade}")

def vender():
    if estoque == []:
        print("Você ainda não cadastrou um produto!")
    else:
        pesquisa = input("Insira o nome do produto que você deseja vender -- ")
        for produto in estoque:
            if pesquisa == produto.nome:
                operacao = int(input("Você deseja vender quantos? -- "))
                if operacao < produto.quantidade:
                    produto.quantidade -= operacao
                    print(f"Produto vendido! Estoque atual -- {produto.quantidade}")
                elif operacao > produto.quantidade:
                    print("Quantidade insuficiente")
                else:
                    estoque.remove(produto)

def menu():
    opcao = int(input("===MENU ESTOQUE===\n1. Cadastrar produto comum\n2. Cadastrar produto alimentício\n3. Listar todos os produtos\n4. Repor estoque\n5. Vender\n6. Sair\n"))
    if opcao == 1:
        cadastrarcomum()
        menu()
    if opcao == 2:
        cadastroalimenticio()
        menu()
    if opcao == 3:
        lista()
        menu()
    if opcao == 4:
        repor()
        menu()
    if opcao == 5:
        vender()
        menu()
    if opcao < 1 or opcao > 6:
        print("Opção inválida!")
        menu()

 
menu()