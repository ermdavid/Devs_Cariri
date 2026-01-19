# 🛍️ Sistema de Loja Virtual Simplificada
**Projeto Final da Disciplina de Programação Orientada a Objetos (POO)**

---

## 📄 Visão Geral

Este projeto tem como objetivo desenvolver um **Sistema de Loja Virtual Simplificada**, utilizando **Python** e os princípios da **Programação Orientada a Objetos (POO)**.  

O sistema funciona por meio de uma **Interface de Linha de Comando (CLI)**, simulando as principais funcionalidades de uma loja virtual, incluindo o cadastro de produtos e clientes, gerenciamento de carrinho de compras, processamento de pedidos e pagamentos, cálculo de frete, emissão de nota/sumário de compra e geração de relatórios de vendas.

Durante o desenvolvimento, foram aplicados os principais pilares da POO, com ênfase em **encapsulamento, herança, composição e validações de regras de negócio**, além de persistência simples de dados.

---

## 💻 Funcionalidades Principais

- Gestão de produtos e controle de estoque;
- Cadastro e gerenciamento de clientes e endereços;
- Carrinho de compras com cálculo de subtotal;
- Processamento de pedidos e pagamentos;
- Cálculo de frete;
- Emissão de nota/sumário de compra;
- Geração de relatórios de vendas.

---

## 🎓 Disciplina e Instituição

- **Disciplina:** Programação Orientada a Objetos (POO)  
- **Período:** 2025.2  
- **Curso:** Tecnologia em Banco de Dados  
- **Instituição:** Universidade Federal do Cariri (UFCA)  
- **Professor:** Dr. Jayr Alencar Pereira  

---

## 👨‍👩‍👧‍👦 Grupo: Devs Cariri

- **Aline Pereira de Lima**  
  Responsável pela implementação do registro de pagamentos, cálculo de frete e aplicação das regras de cupons de desconto.

- **Diego Gomes Pereira**  
  Responsável pelo cadastro de clientes, validação e gerenciamento de endereços.

- **Ermeson David dos Santos Silva**  
  Responsável pela geração de relatórios, implementação da interface CLI e integração geral do sistema.

- **Fernando Pablo Silva Oliveira**  
  Responsável pelo desenvolvimento da classe de produtos e pelo controle de estoque.

- **Rafael Pereira da Silva**  
  Responsável pela implementação do carrinho de compras e pelo cálculo de subtotais.

Este repositório contém o **código-fonte** e a **documentação** do projeto final da disciplina de Programação Orientada a Objetos.

---

## 👤 Principais Classes do Sistema

### 📦 Produto e Estoque
- Classes: `Produto`, `ProdutoFisico`, `ProdutoDigital`
- Responsáveis pelo cadastro, validação, herança entre tipos de produtos e controle de estoque.

### 👤 Cliente e Endereço
- Classes: `Cliente`, `Endereco`
- Gerenciam dados pessoais, validações e associação de endereços.

### 🛒 Carrinho e Pedido
- Classes: `Carrinho`, `ItemCarrinho`, `Pedido`, `ItemPedido`
- Responsáveis pela manipulação de itens, cálculo de subtotais, criação de pedidos e controle de estados.

---

### 💳 Pagamento, Frete e Cupom

#### Classe: Pagamento
- **Atributos:** pedido (Pedido), valor, forma (PIX, Crédito, Débito, Boleto), data  
- **Métodos:** processar, estornar, cancelar  

#### Classe: Cupom
- **Atributos:** código, tipo (Valor ou Percentual), valor, data_validade, uso_maximo, usos_feitos, categorias_elegiveis  
- **Métodos:** validar_uso, calcular_desconto, registrar_uso  

#### Classe: Frete
- **Atributos:** endereço (cidade, UF, CEP), valor, prazo  
- **Métodos:** buscar_regra, calcular_preview (cálculo do valor e prazo estimado)

---

## 🖥️ Interface CLI, Persistência e Relatórios

- Integração entre os módulos do sistema;
- Interface via **linha de comando (CLI)**;
- Persistência de dados em arquivos JSON;
- Geração de relatórios de vendas e financeiros;
- Arquivos de configuração (`settings.json`);
- Documentação do projeto (`README.md`).

## 🧭 Passo a Passo de Execução do Projeto

### ✅ Pré-requisitos
- Python 3.10 ou superior

Verifique a versão do Python:
```bash
python --version
```
### ▶️ Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/ermdavid/Devs_Cariri.git
```
2. Acesse a pasta do projeto:
```bash
cd Devs_Cariri
```
3. Execute o sistema:
```bash
python main.py
```
