from src.repositorios.repositorio_pedidos import RepositorioPedidos

def gerar_relatorio_pedidos():
    repo = RepositorioPedidos()
    pedidos = repo.listar_pedidos()

    with open("relatorio_pedidos.txt", "w", encoding="utf-8") as f:
        for p in pedidos:
            f.write(
                f"Pedido {p.id} | "
                f"Cliente: {p.cliente.nome} | "
                f"Status: {p.status.value} | "
                f"Total: R$ {p.calcular_total():.2f}\n"
            )

    print("Relatório de pedidos gerado.")
