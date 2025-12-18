# 🛍️ Sistema de Loja Virtual Simplificada
**Projeto Final da Disciplina de Programação Orientada a Objetos (POO)**

## 📄 Visão Geral
O objetivo principal deste projeto é desenvolver um sistema de linha de comando (CLI) ou API mínima (FastAPI/Flask, opcional) para uma loja virtual: cadastro de produtos e clientes, carrinho, pedido, pagamento, cálculo de frete, emissão de nota/sumário de compra e relatórios de vendas, utilizando conceitos e pilares de POO, enfatizando herança, encapsulamento, validações e composição. 

## 💻 Funcionalidades Principais 

• Gestão de produtos e clientes;

• Carrinho de compras;

• Processamento de pedidos e pagamento;

• Cálculo de frete;

• Emissão de nota de compra;

• Relatórios de vendas.

## 🎓 Disciplina e Instituição
• Disciplina: Programação Orientada a Objetos (POO)

• Período: 2025.2

• Curso: Tecnologia em Banco de Dados

• Instituição: Universidade Federal do Cariri (UFCA)

• Professor: Dr. Jayr Alencar Pereira

## 👨‍👩‍👧‍👦 Grupo: Devs Cariri 

• Aline Pereira de Lima – responsável pela implementação do registro de pagamentos, cálculo de frete e aplicação das regras de cupons de desconto.

• Diego Gomes Pereira – responsável pelo cadastro de clientes, validação e gerenciamento de endereços.

• Ermeson David dos Santos Silva – responsável pela geração de relatórios, implementação da interface CLI e integração geral do sistema.

• Fernando Pablo Silva Oliveira – responsável pelo desenvolvimento da classe de produtos e pelo controle de estoque.

• Rafael Pereira da Silva – responsável pela implementação do carrinho de compras e pelo cálculo de subtotais.

Este repositório contém o **código-fonte** e a **documentação** do projeto final da disciplina de POO. 


## 👤 Principais Classes do Sistema

📦 Produto e Estoque 
Classes: Produto, ProdutoFisico, ProdutoDigital

Testes

👤 Cliente e Endereço
Classes: Cliente, Endereco

Testes

🛒 Carrinho e Pedido
Classes: Carrinho, ItemCarrinho, Pedido, ItemPedido

Testes

💳 Pagamento, Frete e Cupom
Class: Pagamento
Atributos: data, forma (PIX, Crédito, Débito, Boleto), valor
Métodos: validar, confirmar, estornar

Class: Cupom
Atributos: código, tipo (Valor ou Percentual), valor, data_validade, uso_maximo, usos_feitos, categorias_elegiveis
Métodos: validar, expirado, esgotado, calcular_desconto, registrar_uso

Class: Frete
Atributos: uf, cidade, cep, valor, prazo 
Métodos: tem_frete, calcular_valor, calcular_prazo, 


🖥️ Interface CLI, Persistência e Relatórios

Integração entre os módulos do sistema; 
Interface via linha de comando (CLI);
Persistência de dados (dados.py);
Geração de relatórios;
Arquivos de configuração (settings.json);
Documentação do projeto (README.md)
