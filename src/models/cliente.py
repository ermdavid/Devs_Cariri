class Cliente:
    def __init__(self, id, nome, email, cpf):
        self.id = id
        self.nome = nome
        self._email = email  # Privado para usar @property
        self._cpf = cpf      # Privado para usar @property
        self.enderecos = []  # Lista de objetos da classe Endereco

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.cpf == other.cpf or self.email == other.email
        return False