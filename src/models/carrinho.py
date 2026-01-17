from produto import Produto
from produto_digital import ProdutoDigital
from produto_fisico import ProdutoFisico

class ItemCarrinho: #Rafael Pereira

    def __init__(self, produto, quantidade: int):
        self._produto = produto
        self.quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor: int):
        if valor <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self._quantidade = valor

    @property
    def produto(self):
        return self._produto

    def calcular_subtotal_item(self) -> float:
        # O subtotal considera o preço unitário do produto * quantidade
        return self._produto.preco_unitario * self._quantidade

    def __repr__(self):
        return f"{self._produto.nome} (x{self._quantidade}) - R$ {self.calcular_subtotal_item():.2f}"


class Carrinho:
    """
    Gerencia a coleção de itens selecionados pelo cliente.
    """

    def __init__(self):
        self._itens = []  # Lista de objetos ItemCarrinho

    def adicionar_item(self, produto, quantidade: int):
        # Verifica se o produto já existe no carrinho para apenas somar a quantidade
        for item in self._itens:
            if item.produto.sku == produto.sku:
                item.quantidade += quantidade
                return

        # Caso contrário, cria um novo item
        novo_item = ItemCarrinho(produto, quantidade)
        self._itens.append(novo_item)

    def remover_item(self, produto_id: int):
        self._itens = [
            item for item in self._itens if item.produto.id != produto_id]

    def esvaziar_carrinho(self):
        self._itens = []

    def calcular_subtotal_total(self) -> float:
        """
        Soma o subtotal de todos os itens antes de frete ou cupons.
        """
        return sum(item.calcular_subtotal_item() for item in self._itens)

    @property
    def itens(self):
        return self._itens

    def __len__(self):
        return sum(item.quantidade for item in self._itens)

