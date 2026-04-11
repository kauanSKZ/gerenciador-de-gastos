# Gerenciador de Gastos Pessoais CLI

**Autor:** Kauan Rodrigues da Silva  
**Disciplina:** Bootcamp II 
**Versão:** 1.0.0  
**Repositório:** https://github.com/kauanSKZ/gerenciador-de-gastos

## 1. Descrição do Problema
Muitas pessoas perdem o controle financeiro por não anotarem pequenos gastos diários. Este projeto resolve a "dor" da desorganização financeira através de uma ferramenta rápida e acessível via terminal.

## 2. Proposta da Solução
Uma aplicação em Python que permite registrar gastos (descrição e valor), listar o histórico e visualizar o total acumulado, utilizando persistência de dados em formato JSON.

## 3. Público-alvo
Estudantes e profissionais que buscam uma ferramenta simples e leve para controle de despesas sem necessidade de interfaces complexas ou internet.

## 4. Funcionalidades
- Cadastro de gastos com validação de valores.
- Listagem completa de itens salvos.
- Soma automática do total de despesas.
- Persistência de dados local.

## 5. Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Testes:** Pytest
- **Qualidade/Lint:** Flake8
- **CI/CD:** GitHub Actions

## 6. Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie a aplicação: `python src/main.py`

## 7. Desenvolvimento (Testes e Lint)
- Para rodar os testes: `pytest tests/`
- Para rodar o linter: `flake8 src/ tests/`