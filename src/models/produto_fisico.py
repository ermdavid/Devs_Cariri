from produto import Produto
class ProdutoFisico(Produto):
  def __init__(self, sku:str, nome:str, categoria:str, preco_unitario:float = 0.0, quantidade_estoque:int = 0, peso_kg:float = 0.0, situacao = "ativo", **kwargs):
    super().__init__(sku, nome, categoria, preco_unitario, quantidade_estoque, situacao)
    self.peso_kg = peso_kg

#Propriedade dos atributos 
  @property
  def peso_kg(self) -> float:
    return self._peso_kg
  @peso_kg.setter
  def peso_kg(self, peso_kg:float):
    if not isinstance(peso_kg, (int, float)):
      raise ValueError("O peso deve ser um número")
    self._peso_kg = float(peso_kg) # Correção: Adicionado a atribuição do valor

#Métodos
  def adicionar_estoque(self, quantidade_estoque):
    super().adicionar_estoque(quantidade_estoque)

  def remover_estoque(self, quantidade_estoque):
    super().remover_estoque(quantidade_estoque)

  def calcular_preço_peso(self):
    if self.peso_kg <= 0.5:
      return self.preco_unitario * 0.3
    if self.peso_kg <= 1:
      return self.preco_unitario * 0.5
    if self.peso_kg <= 2:
      return self.preco_unitario * 0.7
    else:
      return self.preco_unitario * 0.9

  def __str__(self):
    exibir_detalhes = super().__str__()
    return f'{exibir_detalhes}| Tipo: físico| Peso: {self.peso_kg}'
