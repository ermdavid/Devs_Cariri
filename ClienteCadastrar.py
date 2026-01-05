class ClienteCadastrar:
       def __init__(self, nome, email, telefone):
            self.nome = nome
            self.email = email
            self.telefone = telefone
            self.Endereco = []

      def cadastrar(self):
            # Lógica para cadastrar o cliente no sistema
            print(f"Cliente {self.nome} cadastrado com sucesso!")
