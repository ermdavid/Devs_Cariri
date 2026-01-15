from cli.menu import menu, executar

def main():
    while True:
        menu()
        opcao = input("Escolha: ")
        if opcao == "0":
            break
        executar(opcao)

if __name__ == "__main__":
    main()
