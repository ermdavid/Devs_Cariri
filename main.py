from datetime import date, timedelta

from src.models.cliente import Cliente
from src.models.cupom import Cupom
from src.models.produto import Produto


def teste_cliente():
    print("\n#### TESTE CLASSE CLIENTE ####")

    print("\nCriação de cliente:")
    cliente1 = Cliente(1, "Ana Silva", "ana.silva@example.com", "11122233344")
    print(f"Cliente 1: {cliente1}")

    print("\nAtualização de email e CPF (testando setters com validação):")
    cliente1.email = "ana.silva.novo@example.com"
    cliente1.cpf = "11122233355"
    print(f"Email do Cliente 1 atualizado: {cliente1.email}")
    print(f"CPF do Cliente 1 atualizado: {cliente1.cpf}")
    print(f"Cliente 1: {cliente1}")

    print("\nCriação de cliente 2:")
    cliente2 = Cliente(2,"Diego Souza", "diego.souza@example.com", "11111111111")
    print(f"Cliente 2: {cliente2}")

    print("\nTeste de __eq__:")
    if cliente1 == cliente2:
        print("Clientes iguais (não esperado)")
    else:
        print("Cliente 1 e Cliente 2 são diferentes (Esperado!)")


def teste_cupom():
    print("\n#### TESTE CLASSE CUPOM ####")

    print("\nCriação de Cupom PERCENTUAL:")
    cupom_percentual = Cupom(
        codigo="DESC10PERC",
        tipo="PERCENTUAL",
        valor=10.0,
        data_validade=date.today() + timedelta(days=30),
        uso_maximo=5,
        usos_feitos=0
    )
    print(f"Cupom PERCENTUAL criado: {cupom_percentual}")

    valor_pedido = 200.0
    desconto = cupom_percentual.calcular_desconto(valor_pedido)
    print(
        f"Pedido de R${valor_pedido:.2f}. "
        f"Desconto de {cupom_percentual.valor}%: R${desconto:.2f}. "
        f"Valor final: R${valor_pedido - desconto:.2f}"
    )

    print("\nCriação de Cupom VALOR:")
    cupom_valor = Cupom(
        codigo="DESC20VALOR",
        tipo="VALOR",
        valor=20.0,
        data_validade=date.today() + timedelta(days=30),
        uso_maximo=3,
        usos_feitos=0
    )
    print(f"Cupom VALOR criado: {cupom_valor}")

    for valor_pedido in [110.0, 50.0, 80.0]:
        desconto = cupom_valor.calcular_desconto(valor_pedido)
        print(
            f"Pedido de R${valor_pedido:.2f}. "
            f"Cupom fixo de R${cupom_valor.valor:.2f}. "
            f"Desconto aplicado: R${desconto:.2f}. "
            f"Valor final: R${valor_pedido - desconto:.2f}"
        )

    print("\nTeste de registrar_uso e validação de limite:")
    cupom_percentual.registrar_uso()
    print(f"Usos feitos do cupom PERCENTUAL: {cupom_percentual.usos_feitos}")

    for _ in range(3):
        try:
            cupom_valor.registrar_uso()
        except ValueError as e:
            print(f"Erro esperado: {e}")

    print(f"Usos feitos do cupom VALOR: {cupom_valor.usos_feitos}")

    print("\nTeste de cupom expirado:")
    try:
        Cupom(
            codigo="EXPIRADO",
            tipo="VALOR",
            valor=10,
            data_validade=date.today() - timedelta(days=1),
            uso_maximo=1,
            usos_feitos=0
        )
    except ValueError as e:
        print(f"Esperado erro de cupom expirado: {e}")

    print("\nTeste de cupom com categorias elegíveis:")
    cupom_categoria = Cupom(
        codigo="TECHPROMO",
        tipo="PERCENTUAL",
        valor=15,
        data_validade=date.today() + timedelta(days=30),
        uso_maximo=2,
        usos_feitos=0,
        categorias_elegiveis=["ELETRONICOS"]
    )

    try:
        cupom_categoria.registrar_uso("ELETRONICOS")
        print("Validação de cupom por categoria 'Eletronicos' bem-sucedida (Esperado!)")
        print(f"Usos feitos do cupom 'TECHPROMO': {cupom_categoria.usos_feitos}")
    except ValueError as e:
        print(e)

    try:
        cupom_categoria.registrar_uso("MODA")
    except ValueError as e:
        print(f"Esperado erro de categoria inválida: {e}")

    print("\nTeste de __eq__:")
    cupom_igual = Cupom(
        codigo="DESC10PERC",
        tipo="PERCENTUAL",
        valor=10,
        data_validade=date.today() + timedelta(days=10),
        uso_maximo=1,
        usos_feitos=0
    )

    if cupom_percentual == cupom_igual:
        print("Cupom PERCENTUAL e cupom_igual são considerados iguais por código (Esperado!)")


def teste_produto():
    print("\n#### TESTE CLASSE PRODUTO ####")

    print("\nCriação de Produto e acesso a atributos:")
    produto_a = Produto("P001", "Cadeira Gamer", 899.90, 10)
    print(f"Produto A criado: {produto_a}")

    print("\nAtualização de atributos:")
    produto_a.preco = 799.90
    produto_a.situacao = "promocao"
    print(f"Produto A atualizado: Preço: R${produto_a.preco}, Situação: {produto_a.situacao}")

    print("\nTeste de SKU duplicado:")
    try:
        Produto("P001", "Produto Duplicado", 100, 1)
    except ValueError as e:
        print(f"Esperado erro de SKU duplicado: {e}")

    print("\nTeste de __eq__ e __ne__:")
    produto_clone = Produto("P001", "Cadeira Gamer Clone", 799.90, 5)
    produto_b = Produto("P002", "Mesa Gamer", 599.90, 8)

    if produto_a == produto_clone:
        print("Produto A e Produto A Clone são considerados iguais por SKU (Esperado!)")

    if produto_a != produto_b:
        print("Produto A e Produto B são diferentes (Esperado!)")


def main():
    teste_cliente()
    teste_cupom()
    teste_produto()


if __name__ == "__main__":
    main()
