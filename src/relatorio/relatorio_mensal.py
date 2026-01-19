from datetime import date
from src.repositorios.repositorio_pedidos import RepositorioPedidos
from src.utils.enums import StatusPedido

def gerar_relatorio_mensal(ano: int, mes: int):
    repo = RepositorioPedidos()
    total = 0.0

    with open(f"relatorio_mensal_{ano}_{mes:02d}.txt", "w", encoding="utf-8") as f:
        for p in repo.listar_pedidos():
            if p.data_criacao.year == ano and p.data_criacao.month == mes:
                if p.status in (StatusPedido.PAGO, StatusPedido.ENTREGUE):
                    total += p.calcular_total()
                    f.write(
                        f"Pedido {p.id} | "
                        f"Total: R$ {p.calcular_total():.2f}\n"
                    )

        f.write(f"\nTOTAL DO MÊS: R$ {total:.2f}")

    print("Relatório mensal gerado.")
