from carrinho import Carrinho
from cliente import Cliente
from endereco import Endereco
from frete import Frete
from pagamento import Pagamento
from produto import Produto

class pagar_pedido(Pagamento):
  def __init__(self, pedido, valor: float, forma: FormaPagamento, data=None):
    super().__init__(pedido, valor, forma, data)
  def processar(self):
    return super().processar()
  def estornar(self):
    return super().estornar()
  def cancelar_pagamento(self):
    return super().cancelar_pagamento()
class Pedido:
    _STATUS_VALIDOS = ['criado', 'pago', 'enviado', 'entregue', 'cancelado']

    def __init__(self, cliente: Cliente, carrinho: Carrinho, frete: Frete):
      self.cliente = cliente
      self.carrinho = carrinho._itens.copy()
      self.frete = frete
      self._status = 'criado' # Status inicial do pedido
      self.pagamento = None # Initialize pagamento to None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status: str):
        if novo_status not in self._STATUS_VALIDOS:
            raise ValueError(f"Status inválido: {novo_status}. Status permitidos são {', '.join(self._STATUS_VALIDOS)}.")
        self._status = novo_status

    def calcular_subtotal_carrinho(self):
        return sum(item.calcular_subtotal_item() for item in self.carrinho)

    def calcular_total_pedido(self):
      tem_produto_fisico = any(isinstance(item.produto, ProdutoFisico) for item in self.carrinho)
      if tem_produto_fisico:
        return self.calcular_subtotal_carrinho() + self.frete.valor
      else:
        return self.calcular_subtotal_carrinho()

    def exibir_pedido(self):
      print(f"Status do pedido: {self.status}")
      print(f"Cliente: {self.cliente.nome}")

    def criar_pedido(self):
      self.status = "criado"
      tem_produto_fisico = any(isinstance(item.produto, ProdutoFisico) for item in self.carrinho)
      for item in self.carrinho:
        prod = item.produto
        print(f"SKU: {prod.sku}")
        print(f"Nome: {prod.nome}")
        print(f"Preço: {prod.preco_unitario}")
        print(f"Quantidade: {item.quantidade}")
        print(f"Subtotal: {item.calcular_subtotal_item()}")
        print()
      if tem_produto_fisico:
        print("--- Detalhes do Frete ---")
        print(f"Valor do Frete: {self.frete.valor}")
        print(f"Prazo de Entrega: {self.frete.prazo} dias")
        print()
      return (f"Valor Total: {self.calcular_total_pedido()}. Status atualizado: pedido {self.status}")

    def pagar_pedido(self, pagamento_obj):
      if pagamento_obj.processar():
          self.status = "pago"
          self.pagamento = pagamento_obj # Store the payment object
          return True
      return False

    def enviar_pedido(self):
      self.status = "enviado"
      return (f"O pedido no valor total: {self.calcular_total_pedido()} foi enviado. Status atualizado: pedido {self.status}")

    def entregar_pedido(self):
      self.status = "entregue"
      return (f"O pedido no valor total: {self.calcular_total_pedido()} foi enviado. Status atualizado: pedido {self.status}")

    def cancelar_pedido(self, pagamento_obj):
      if self.status == "criado":
        self.status = "cancelado"
        return (f"Valor Total: {self.calcular_total_pedido()}. Status atualizado: pedido {self.status}")
      elif self.status == "pago":
        try:
            pagamento_obj.estornar()
            self.status = "cancelado"
            return (f"Valor Total: {self.calcular_total_pedido()}. Status atualizado: pedido {self.status}")
        except ValueError as e:
            return (f"Não foi possível cancelar o pedido: {e}. Status atual: {self.status}")
      else:
        return (f"O pedido não pode ser mais cancelado. Status atual: {self.status}")

    def gerar_resumo_textual(self) -> str:
        resumo = f"--- Resumo do Pedido ---\n"
        resumo += f"Status: {self.status.capitalize()}\n"
        resumo += f"Cliente: {self.cliente.nome} ({self.cliente.email})\n\n"

        resumo += "Itens do Pedido:\n"
        for item in self.carrinho:
            resumo += (
                f"  - {item.produto.nome} (SKU: {item.produto.sku}) x {item.quantidade} "
                f"(R$ {item.produto.preco_unitario:.2f} cada) = R$ {item.calcular_subtotal_item():.2f}\n"
            )
        resumo += f"Subtotal do Carrinho: R$ {self.calcular_subtotal_carrinho():.2f}\n\n"

        tem_produto_fisico = any(isinstance(item.produto, ProdutoFisico) for item in self.carrinho)
        if tem_produto_fisico:
            resumo += f"Detalhes do Frete:\n"
            resumo += f"  Valor: R$ {self.frete.valor:.2f}\n"
            resumo += f"  Prazo de Entrega: {self.frete.prazo} dias\n\n"
        else:
            resumo += "Detalhes do Frete: Não aplicável (apenas produtos digitais)\n\n"

        resumo += f"Valor Total do Pedido: R$ {self.calcular_total_pedido():.2f}\n\n"

        resumo += "Endereço de Entrega:\n"
        resumo += f"  Rua: {self.frete.endereco.rua}, Número: {self.frete.endereco.numero}\n"
        resumo += f"  Cidade: {self.frete.endereco.cidade} - {self.frete.endereco.estado}\n"
        resumo += f"  CEP: {self.frete.endereco.cep}\n\n"

        resumo += "Informações de Pagamento:\n"
        if self.pagamento:
            resumo += f"  Forma de Pagamento: {self.pagamento.forma.value}\n"
            resumo += f"  Status do Pagamento: {self.pagamento.status.value}\n"
            resumo += f"  Valor Pago: R$ {self.pagamento.valor:.2f}\n"
            resumo += f"  Data do Pagamento: {self.pagamento.data.strftime('%d/%m/%Y %H:%M:%S')}\n"
        else:
            resumo += "  Pagamento ainda não processado ou pendente.\n"

        return resumo
