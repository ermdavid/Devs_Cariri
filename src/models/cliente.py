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
        if "@" not in valor:  # Validação simplificada
            raise ValueError("Email inválido")
        self._email = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        # verificação simples
        if not valor.isdigit():
            raise ValueError("CPF deve conter apenas números")
        self._cpf = valor

    def adicionar_endereco(self, endereco):
        """Adiciona um endereço à lista de endereços do cliente"""
        if endereco not in self.enderecos:
            self.enderecos.append(endereco)
            # Vincula o cliente ao endereço se ainda não estiver vinculado
            if endereco.cliente != self:
                endereco.cliente = self
        else:
            raise ValueError("Endereço já cadastrado para este cliente")

    def remover_endereco(self, endereco):
        """Remove um endereço da lista de endereços do cliente"""
        if endereco in self.enderecos:
            self.enderecos.remove(endereco)
        else:
            raise ValueError("Endereço não encontrado na lista do cliente")

    def listar_enderecos(self):
        """Retorna a lista de endereços do cliente"""
        return self.enderecos

    def buscar_endereco_por_id(self, id_endereco):
        """Busca um endereço pelo ID"""
        for endereco in self.enderecos:
            if endereco.id == id_endereco:
                return endereco
        return None

    def quantidade_enderecos(self):
        """Retorna a quantidade de endereços cadastrados"""
        return len(self.enderecos)

    def to_dict(self):
        """Converte o cliente para um dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'enderecos': [endereco.to_dict() for endereco in self.enderecos]
        }
