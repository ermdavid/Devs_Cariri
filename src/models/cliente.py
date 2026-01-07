class Cliente:
    """Classe onde com atributos para identificação do cliente"""
    def __init__(self, id, nome, email, cpf):
        self.id = id
        self.nome = nome
        self._email = email  # Privado para usar @property
        self._cpf = cpf      # Privado para usar @property
        self.enderecos = []  # Lista de objetos da classe Endereco

    def __eq__(self, other):
        """Ferifica se o email ou o CPF já foram cadastrados"""
        if isinstance(other, Cliente):
            return self.cpf == other.cpf or self.email == other.email
        return False

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor: # Validação simplificada
            raise ValueError("Email inválido")
        self._email = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
#verificação simples
        if not valor.isdigit(): 
            raise ValueError("CPF deve conter apenas números")
        self._cpf = valor
