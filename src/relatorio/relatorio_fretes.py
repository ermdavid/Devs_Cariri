from src.repositorios.repositorio_pedidos import RepositorioPedidos

def gerar_relatorio_fretes():
    repo = RepositorioPedidos()
    pedidos = repo.listar_pedidos()

    with open("relatorio_fretes.txt", "w", encoding="utf-8") as f:
        for p in pedidos:
            if p.frete:
                f.write(
                    f"Pedido {p.id} | "
                    f"Cidade: {p.endereco_entrega.cidade} | "
                    f"Frete: R$ {p.valor_frete:.2f}\n"
                )

    print("Relatório de fretes gerado.")
