from src.reports.faturamento import relatorio_faturamento
from src.reports.produtos import relatorio_produtos_mais_vendidos
from src.reports.pedidos import relatorio_pedidos_por_status


def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("1 - Faturamento por período")
        print("2 - Produtos mais vendidos")
        print("3 - Pedidos por status")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inicio = input("Data início (YYYY-MM-DD): ")
            fim = input("Data fim (YYYY-MM-DD): ")
            relatorio_faturamento(inicio, fim)
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            relatorio_produtos_mais_vendidos()
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            relatorio_pedidos_por_status()
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")
