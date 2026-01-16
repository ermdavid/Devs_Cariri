from repository import clientes, produtos
from models.cliente import Cliente
from models.produto import Produto
from reports.relatorio_vendas import relatorio_vendas

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
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                print(p)

    elif opcao == "4":
        relatorio_vendas()

    elif opcao == "0":
        print("Encerrando o sistema...")

    else:
        print("Opção inválida!")
