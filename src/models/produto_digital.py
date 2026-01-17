from produto import Produto
class ProdutoDigital(Produto):
  def __init__(self, sku:str, nome:str, categoria:str, preco_unitario:float = 0.0, quantidade_estoque:int = 0, tamanho_mb:float = 0.0, situacao = "ativo", **kwargs):
    super().__init__(sku, nome, categoria, preco_unitario, quantidade_estoque, situacao)
    self.tamanho_mb = tamanho_mb

#Propriedade dos atributos
  @property
  def tamanho_mb(self) -> float:
    return self._tamanho_mb
  @tamanho_mb.setter
  def tamanho_mb(self, tamanho_mb:float):
    if not isinstance(tamanho_mb, (int, float)):
      raise ValueError("O tamanho deve ser um número")
    self._tamanho_mb = float(tamanho_mb)

#Métodos
  def adicionar_estoque(self, quantidade_estoque):
    super().adicionar_estoque(quantidade_estoque)

  def remover_estoque(self, quantidade_estoque):
    super().remover_estoque(quantidade_estoque)

  def __str__(self):
    exibir_detalhes = super().__str__()
    return f'{exibir_detalhes}| Tipo: digital| Tamanho: {self.tamanho_mb}mb'
