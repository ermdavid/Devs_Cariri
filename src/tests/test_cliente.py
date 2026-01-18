import pytest
from src.models.cliente import Cliente
from src.models.endereco import Endereco

def test_criacao_cliente_valido():
    cliente = Cliente(1, "Ana Silva", "ana.silva@example.com", "11122233344")
    assert cliente.nome == "Ana Silva"
    assert cliente.email == "ana.silva@example.com"
    assert cliente.cpf == "11122233344"
    assert cliente.quantidade_enderecos() == 0

def test_setters_email_cpf_validos():
    cliente = Cliente(2, "Carlos", "carlos@example.com", "12345678901")
    cliente.email = "novo.email@example.com"
    cliente.cpf = "98765432100"
    assert cliente.email == "novo.email@example.com"
    assert cliente.cpf == "98765432100"

def test_email_invalido_gera_erro():
    with pytest.raises(ValueError):
        Cliente(3, "Erro Email", "email_invalido", "12345678901")

def test_cpf_invalido_gera_erro():
    with pytest.raises(ValueError):
        Cliente(4, "Erro CPF", "teste@example.com", "abc123")

def test_clientes_iguais_por_cpf():
    c1 = Cliente(5, "João", "joao1@example.com", "11111111111")
    c2 = Cliente(6, "João Clone", "joao2@example.com", "11111111111")
    assert c1 == c2

def test_adicionar_endereco():
    cliente = Cliente(7, "Lúcia", "lucia@example.com", "22222222222")
    endereco = Endereco(1, "63000000", "Juazeiro do Norte", "CE", "Rua A", 100)
    cliente.adicionar_endereco(endereco)
    assert cliente.quantidade_enderecos() == 1
    assert endereco in cliente.listar_enderecos()
    assert endereco.cliente == cliente

def test_endereco_duplicado_gera_erro():
    cliente = Cliente(8, "Rafael", "rafael@example.com", "33333333333")
    endereco = Endereco(2, "63000000", "Crato", "CE", "Rua B", 200)
    cliente.adicionar_endereco(endereco)
    with pytest.raises(ValueError):
        cliente.adicionar_endereco(endereco)

def test_remover_endereco():
    cliente = Cliente(9, "Marina", "marina@example.com", "44444444444")
    endereco = Endereco(3, "63000000", "Barbalha", "CE", "Rua C", 300)
    cliente.adicionar_endereco(endereco)
    cliente.remover_endereco(endereco)
    assert cliente.quantidade_enderecos() == 0

  
