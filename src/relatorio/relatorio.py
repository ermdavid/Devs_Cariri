from repository import pedidos

def relatorio_vendas():
    with open("relatorio_vendas.txt", "w", encoding="utf-8") as f:
        for pedido in pedidos:
            f.write(f"Pedido {pedido.id} - Total: R${pedido.total():.2f}\n")

    print("Relatório gerado!")
