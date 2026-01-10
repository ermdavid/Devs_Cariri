class Produto:
  _all_skus = set() # Variável de classe para armazenar todos os SKUs existentes
  def __init__(self, sku:str, nome:str, categoria:str, preco_unitario:float = 0.0, quantidade_estoque:int = 0, situacao = "ativo", **kwargs):
    if sku in Produto._all_skus:
      raise ValueError(f"SKU '{sku}' já existe. Não é possível criar produtos com SKUs duplicados.")

    self._sku = sku # Armazenar internamente o SKU
    Produto._all_skus.add(sku) # Adiciona o SKU ao conjunto de SKUs globais

    self.nome = nome
    self.categoria = categoria
    self.preco_unitario = preco_unitario
    self.quantidade_estoque = quantidade_estoque
    self.situacao = situacao

  @property
  def sku(self) -> str:
    return self._sku

  @property
  def nome(self) -> str:
    return self._nome

  @nome.setter
  def nome(self, nome:str):
    if not isinstance(nome, str) :
      raise ValueError("O nome deve ser uma string")
    if nome == "" or nome.isspace():
      raise ValueError("O nome não pode ser vazio")
    self._nome = nome

  @property
  def preco_unitario(self) -> float:
    return self._preco_unitario

  @preco_unitario.setter
  def preco_unitario(self, preco_unitario:float):
    if not isinstance(preco_unitario, (int, float)):
      raise ValueError("O preço deve ser um número")
    if preco_unitario <= 0:
      raise ValueError("O preço não pode ser negativo")
    self._preco_unitario = float(preco_unitario)

  @property
  def quantidade_estoque(self) -> int:
    return self._quantidade_estoque

  @quantidade_estoque.setter
  def quantidade_estoque(self, quantidade_estoque:int):
    if not isinstance(quantidade_estoque, (int, float)):
      raise ValueError("O estoque deve ser um número")
    if quantidade_estoque < 0:
      raise ValueError("O estoque não pode ser negativo")
    self._quantidade_estoque = int(quantidade_estoque)

  def adicionar_estoque(self, quantidade):
    if quantidade > 0:
      self.quantidade_estoque += quantidade
      print(f"Foi adicionado {quantidade} unidades do produto {self.nome}. Estoque atual: {self.quantidade_estoque}")
    else:
      print("A quantidade deve ser maior que zero.")

  def remover_estoque(self, quantidade):
    if quantidade > 0:
      if self.quantidade_estoque >= quantidade:
        self.quantidade_estoque -= quantidade
        print(f"Foram removidas {quantidade} unidades do produto {self.nome}. Estoque atual: {self.quantidade_estoque}")
      else:
        print(f"Não há {quantidade} unidades disponíveis em estoque para o produto {self.nome}. Estoque atual: {self.quantidade_estoque}")
    else:
      print("A quantidade deve ser maior que zero.")

  def __str__(self):
    return f"Produto: {self.nome} (SKU: {self.sku}, Categoria: {self.categoria}, Preço: {self.preco_unitario}, Estoque: {self.quantidade_estoque}, Situação: {self.situacao})"

  def __repr__(self):
    return f"Produto(sku='{self.sku}', nome='{self.nome}', categoria='{self.categoria}', situacao='{self.situacao}', preco_unitario={self.preco_unitario}, quantidade_estoque={self.quantidade_estoque})"

  def __eq__(self, other):
    if not isinstance(other, Produto):
      return NotImplemented
    return self.sku == other.sku

  def __ne__(self, other):
    return not self.__eq__(other)

  @classmethod
  def clear_all_skus(cls):
    """Limpa o registro de todos os SKUs (útil para testes)."""
    cls._all_skus.clear()
