import requests
import json
import os
try:
    from src.database import supabase
except ImportError:
    from database import supabase

__version__ = "1.0.0"
ARQUIVO_DADOS = "gastos.json"


def carregar_gastos():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def salvar_gastos(gastos):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)


def adicionar_gasto(descricao, valor):
    if not descricao.strip():
        raise ValueError("A descrição não pode estar vazia.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    supabase.table("gastos").insert(
        {"descricao": descricao, "valor": valor}
    ).execute()
    return True


def calcular_total():
    resposta = supabase.table("gastos").select("valor").execute()
    gastos = resposta.data
    return sum(item['valor'] for item in gastos)


def obter_cotacao_dolar():
    try:
        resposta = requests.get(
            "https://economia.awesomeapi.com.br/last/USD-BRL"
        )
        resposta.raise_for_status()
        dados = resposta.json()
        cotacao = float(dados["USDBRL"]["bid"])
        return cotacao
    except Exception:
        return None


def listar_gastos():
    try:
        resposta = supabase.table("gastos").select("*").execute()
        gastos = resposta.data

        if not gastos:
            print("Nenhum gasto cadastrado no banco de dados.")
            return

        print("\n=== LISTA DE GASTOS (SUPABASE) ===")

        for gasto in gastos:
        print(
        f"ID: {gasto['id']} | "
        f"Descrição: {gasto['descricao']} | "
        f"Valor: R$ {gasto['valor']}"
        )

        print("==============================\n")

    except Exception as e:
        print(f"Erro ao buscar gastos: {e}")


def filtrar_gastos_altos(valor_limite: float):
    try:
        resposta = supabase.table("gastos").select("*").gt(
            "valor", valor_limite
        ).execute()
        gastos_filtrados = resposta.data

        if not gastos_filtrados:
            print(f"Nenhum gasto cadastrado acima de R${valor_limite:.2f}")
            return

        print(f"\n--- GASTOS ACIMA DE R$ {valor_limite:.2f} ---")
        for g in gastos_filtrados:
            print(f"- {g['descricao']}: R$ {g['valor']:.2f}")

    except Exception as e:
        print(f"Erro ao filtrar dados: {e}")


def menu():
    while True:
        print(f"\n=== GERENCIADOR DE GASTOS v{__version__}===")
        print("1. Cadastrar Gasto")
        print("2. Listar Gastos")
        print("3. Filtrar Gastos Altos")
        print("0. Sair")
        opcao = input("\nEscolha uma opção: ")

        opcao = input("Escolha uma opção: ")

if opcao == "1":
    pass
elif opcao == "2":
    pass
elif opcao == "3":
    limite_txt = input("Exibir gastos maiores que quanto (R$)? ")
    limite = float(limite_txt)
    filtrar_gastos_altos(limite)


if _name_ == "_main_":
    menu()

