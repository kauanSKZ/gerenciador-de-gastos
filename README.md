# Gerenciador de Gastos Pessoais CLI

**Autor:** Kauan Rodrigues da Silva, Matheus Pereira, Miguel Oliveira, Iago Tavares e Gabriel Barbosa
**Disciplina:** Bootcamp II | **Versão:** 2.0.0 (Etapa Final - Banco de Dados na Nuvem)  
**Repositório:** [https://github.com/kauanSKZ/gerenciador-de-gastos](https://github.com/kauanSKZ/gerenciador-de-gastos)

---

## 1. Descrição do Problema

Muitas pessoas perdem o controle financeiro por não anotarem pequenos gastos diários. Este projeto resolve a "dor" da desorganização financeira através de uma ferramenta rápida e acessível via terminal.

## 2. Proposta da Solução

Uma aplicação em Python que permite registrar gastos (descrição e valor), listar o histórico de forma organizada e aplicar filtros avançados de busca. O grande diferencial desta etapa final é a migração da persistência de dados: abandonamos o formato JSON local e passamos a utilizar um **Banco de Dados Relacional PostgreSQL hospedado na Nuvem via Supabase**, garantindo segurança e integridade das informações.

---

## 👥 3. Organização da Equipe e Divisão de Tarefas

O planejamento e a execução do projeto seguiram metodologias ágeis de desenvolvimento através do gerenciamento de GitHub Issues e Code Review em Pull Requests (PRs):

* **Kauan Rodrigues (`@kauanSKZ`)** - Responsável pela Infraestrutura e modelagem da tabela no Supabase, configuração inicial do SDK e gerenciamento seguro de Variáveis de Ambiente (Issue #3).
* **[Matheus Pereira] (`Matheus-Pereira1`)** - Responsável pela migração técnica da função de cadastro/escrita de novos gastos diretamente na tabela na nuvem (Issue #4).
* **[Miguel Oliveira] (`miguelDiniz-dev`)** - Responsável pela migração técnica da função de listagem/leitura do histórico de gastos em tempo real do banco de dados (Issue #5).
* **[Iago Tavares] (`iagotavares-coder`)** - Responsável pela atualização e manutenção da esteira de testes automatizados com Pytest adequando-os à nova estrutura de dados (Issue #6).
* **Gabriel Barbosa] (`GabrielGB-markerting`)** - Responsável pelo desenvolvimento da nova funcionalidade de Filtro Avançado para consultas condicionais no banco (Issue #7).

---

## 4. Funcionalidades

* Cadastro de gastos em tempo real na nuvem com validação de valores.
* Listagem completa de itens salvos integrada diretamente ao PostgreSQL remoto.
* Filtro Avançado de gastos (consultas inteligentes baseadas no valor).
* Soma automática do total de despesas acumuladas.

## 5. Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Banco de Dados:** Supabase (PostgreSQL Cloud)
* **Testes:** Pytest
* **Qualidade/Lint:** Flake8
* **CI/CD:** GitHub Actions (Garantia de esteiras verdes automatizadas antes de cada Merge)
* **Segurança:** Python-dotenv (Gerenciamento seguro de credenciais por arquivos `.env`)

---

## 6. Como Executar

### 1. Configurar as Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto e adicione as credenciais do banco fornecidas pelo administrador:
```text
SUPABASE_URL= https://svautfjtadyqzgrlally.supabase.co
SUPABASE_KEY= sb_publishable_GzMji_gTC726oElSp_VMUA_biLixeY9
