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
        print("==================================\n")

    except Exception as e:
        print(f"Erro ao buscar gastos: {e}")

def filtrar_gastos_altos(valor_limite):
    gastos = carregar_gastos()

    encontrados = False

    print(f"\n--- GASTOS ACIMA DE R$ {valor_limite:.2f} ---")

    for gasto in gastos:
        if gasto["valor"] > valor_limite:
            print(
                f"{gasto['descricao']} - R$ {gasto['valor']:.2f}"
            )
            encontrados = True

    if not encontrados:
        print("Nenhum gasto encontrado.")
main


def menu():
    while True:
        print(f"\n=== GERENCIADOR DE GASTOS v{__version__}===")
        print("1. Adicionar Novo Gasto")
        print("2. Listar Todos os Gastos")
        print("3. Exibir Total Acumulado")
        print("4. Filtrar Gastos Altos")
        print("5. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            desc = input("Descrição do gasto: ")
            try:
                val = float(input("Valor (ex: 50.25): R$ "))
                adicionar_gasto(desc, val)
                print("Gasto registrado!")
            except ValueError:
                print("Valor inválido.")
        elif opcao == '2':
            listar_gastos()
        elif opcao == '3':
            print(f"\n TOTAL GERAL: R$ {calcular_total():.2f}")
            cotacao = obter_cotacao_dolar()
            if cotacao:
                total_dolar = calcular_total() / cotacao
                print(f" TOTAL EM DÓLAR: US$ {total_dolar:.2f} "
                      f"(Cotação: R$ {cotacao:.2f})")
            else:
                print(" [Aviso: Cotação do dólar indisponível no momento]")
        elif opcao == "4":
            valor = float(
                input("Mostrar gastos acima de R$: ")
            )

            filtrar_gastos_altos(valor)

        elif opcao == "5":
            print("Encerrando...")
            break
        else:
    print("Opção inválida.")


if __name__ == "__main__":
    menu()
