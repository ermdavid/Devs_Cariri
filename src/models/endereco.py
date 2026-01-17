from cliente import Cliente
class Endereco:
    """Classe onde com atributos para identificação do endereço"""
    def __init__(self, id, cliente: Cliente, rua, numero, cidade, estado, cep):
        self.id = id
        self.cliente = cliente  # Associação com a classe Cliente
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep    