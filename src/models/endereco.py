from cliente import Cliente
import re


class Endereco:
    """Classe onde com atributos para identificação do endereço"""

    def __init__(self, id, cliente: Cliente, rua, numero, cidade, estado, cep, auto_vincular=True):
        self.id = id
        self._cliente = None  # Atributo privado
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self._estado = None  # Atributo privado
        self._cep = None  # Atributo privado

        # Usa os setters para validar
        self.estado = estado
        self.cep = cep

        # Vincula ao cliente (usando property para manter consistência)
        if cliente:
            self.cliente = cliente
            # Adiciona este endereço à lista do cliente automaticamente
            if auto_vincular and self not in cliente.enderecos:
                cliente.enderecos.append(self)

    def __str__(self):
        """Retorna uma representação legível do endereço"""
        return f"{self.rua}, {self.numero}, {self.cidade} - {self.estado}, CEP: {self.cep}"

    def __repr__(self):
        """Retorna uma representação técnica do endereço para debug"""
        return f"Endereco(id={self.id}, rua='{self.rua}', numero='{self.numero}', cidade='{self.cidade}', estado='{self.estado}', cep='{self.cep}')"

    @property
    def cliente(self):
        """Getter para o cliente"""
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        """Setter para o cliente"""
        if valor is None:
            raise ValueError("Cliente não pode ser None")
        self._cliente = valor

    @property
    def cep(self):
        """Getter para o CEP"""
        return self._cep

    @cep.setter
    def cep(self, valor):
        """
        Setter para o CEP com validação automática
        Aceita formatos: 12345-678 ou 12345678
        """
        if not valor:
            raise ValueError("CEP não pode ser vazio")

        # Remove espaços em branco
        cep_limpo = str(valor).strip().replace(" ", "")

        # Verifica padrão com hífen (12345-678) ou sem hífen (12345678)
        padrao_com_hifen = r'^\d{5}-\d{3}$'
        padrao_sem_hifen = r'^\d{8}$'

        if not (re.match(padrao_com_hifen, cep_limpo) or re.match(padrao_sem_hifen, cep_limpo)):
            raise ValueError(
                f"CEP inválido: {valor}. Use o formato 12345-678 ou 12345678")

        self._cep = cep_limpo

    @property
    def estado(self):
        """Getter para o estado"""
        return self._estado

    @estado.setter
    def estado(self, valor):
        """
        Setter para o estado com validação automática
        Aceita apenas UFs brasileiras válidas
        """
        ufs_validas = [
            'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
            'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
            'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
        ]

        if not valor:
            raise ValueError("Estado não pode ser vazio")

        estado_upper = str(valor).strip().upper()

        if estado_upper not in ufs_validas:
            raise ValueError(
                f"Estado inválido: {valor}. Use uma UF válida (ex: CE, SP, RJ)")

        self._estado = estado_upper

    def validar_cep(self):
        """
        Valida o formato do CEP atual
        Retorna True se válido, False caso contrário
        """
        if not self._cep:
            return False

        # Remove espaços em branco
        cep_limpo = str(self._cep).strip().replace(" ", "")

        # Verifica padrão com hífen (12345-678) ou sem hífen (12345678)
        padrao_com_hifen = r'^\d{5}-\d{3}$'
        padrao_sem_hifen = r'^\d{8}$'

        return bool(re.match(padrao_com_hifen, cep_limpo) or re.match(padrao_sem_hifen, cep_limpo))

    def validar_estado(self):
        """
        Valida se o estado atual é uma UF brasileira válida
        Retorna True se válido, False caso contrário
        """
        ufs_validas = [
            'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
            'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
            'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
        ]

        if not self._estado:
            return False

        return str(self._estado).strip().upper() in ufs_validas

    def to_dict(self):
        """
        Converte o endereço para um dicionário
        Útil para serialização JSON ou armazenamento
        """
        return {
            'id': self.id,
            'cliente_id': self.cliente.id if self.cliente else None,
            'rua': self.rua,
            'numero': self.numero,
            'cidade': self.cidade,
            'estado': self.estado,
            'cep': self.cep
        }
