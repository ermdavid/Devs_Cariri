from repository import clientes, produtos
from models.cliente import Cliente
from models.produto import Produto

def menu():
    print("\n=== LOJA DevsCariri ===")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Produto")
    print("3 - Listar Produtos")
    print("4 - Gerar Relatório")
    print("0 - Sair")

def executar(opcao):
    if opcao == "1":
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")
        clientes.append(Cliente(id, nome, email, cpf))
        print("Cliente cadastrado!")

    elif opcao == "2":
        sku = input("SKU: ")
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        produtos.append(Produto(sku, nome, categoria, preco, estoque))
        print("Produto cadastrado!")

    elif opcao == "3":
        for p in produtos:
            print(p)
