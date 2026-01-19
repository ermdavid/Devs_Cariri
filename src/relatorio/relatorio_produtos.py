from src.repositorios.repositorio_produtos import RepositorioProdutos

def gerar_relatorio_produtos():
    repo = RepositorioProdutos()
    produtos = repo.listar_produtos()

    with open("relatorio_produtos.txt", "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(
                f"{p.sku} - {p.nome} | "
                f"Categoria: {p.categoria} | "
                f"Preço: R$ {p.preco_unitario:.2f} | "
                f"Estoque: {p.quantidade_estoque}\n"
            )

    print("Relatório de produtos gerado.")
