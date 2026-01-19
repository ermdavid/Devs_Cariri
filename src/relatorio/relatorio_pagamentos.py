from src.repositorios.repositorio_pagamentos import RepositorioPagamentos

def gerar_relatorio_pagamentos():
    repo = RepositorioPagamentos()
    pagamentos = repo.listar_pagamentos()

    with open("relatorio_pagamentos.txt", "w", encoding="utf-8") as f:
        for p in pagamentos:
            f.write(
                f"Pedido {p.pedido.id} | "
                f"Forma: {p.forma.value} | "
                f"Status: {p.status.value} | "
                f"Valor: R$ {p.valor:.2f}\n"
            )

    print("Relatório de pagamentos gerado.")
