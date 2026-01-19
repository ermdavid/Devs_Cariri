from datetime import date
from src.repositorios.repositorio_pedidos import RepositorioPedidos
from src.utils.enums import StatusPedido

def gerar_relatorio_financeiro(data_inicio: date, data_fim: date):
    repo = RepositorioPedidos()
    total = 0.0

    for pedido in repo.listar_pedidos():
        if data_inicio <= pedido.data_criacao.date() <= data_fim:
            if pedido.status in (StatusPedido.PAGO, StatusPedido.ENTREGUE):
                total += pedido.calcular_total()

    with open("relatorio_financeiro.txt", "w", encoding="utf-8") as f:
        f.write(f"Faturamento no período: R$ {total:.2f}")

    print("Relatório financeiro gerado.")
