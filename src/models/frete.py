import json
from pathlib import Path

from endereco import Endereco
from carrinho import Carrinho
from produto_fisico import ProdutoFisico

# localiza o settings.json para armazenar as regras de frete
def carregar_tabela_frete():
    path = Path(__file__).parent.parent / "settings.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)["frete"]

class Frete:
    def __init__(self, endereco: Endereco): #deve receber um atributo da classe Endereço(cidade, uf, cep)
        if not isinstance(endereco, Endereco):
            raise TypeError("endereço deve ser uma instância de Endereco")

        self.endereco = endereco
        self.valor = 0
        self.prazo = 0
        self.tabela_frete = carregar_tabela_frete() #armazena as regras de frete 

    def _buscar_regra(self, tabela_frete):
        cep = self.endereco.cep.replace("-", "")
        for faixa in tabela_frete["faixas_cep"]:
            inicio = faixa["inicio"].replace("-", "")
            fim = faixa["fim"].replace("-", "")
            if inicio <= cep <= fim:
                return faixa
        return tabela_frete["default"]

    def calcular_preview(self, carrinho: Carrinho): #deve receber uma instância da classe Carrinho, que armazena os itens (do tipo ItemCarrinho) numa lista
        if not isinstance(carrinho, Carrinho):
            raise TypeError("carrinho deve ser uma instância de Carrinho")

        #verifica se tem algum produto físico no carrinho
        tem_produto_fisico = any(isinstance(item.produto, ProdutoFisico) for item in carrinho.itens)

        #se houver, guarda o valor e prazo da tabela de acordo com o CEP, se não, o valor permanece 0, pois produto digital não tem frete
        if tem_produto_fisico:
            regra = self._buscar_regra(self.tabela_frete)
            self.valor = regra["valor"]
            self.prazo = regra["prazo"]
        else: 
            self.valor = 0
            self.prazo = 0        

        return {"valor": self.valor, "prazo": self.prazo}

