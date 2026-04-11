import json
import os

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
    gastos = carregar_gastos()
    gastos.append({"descricao": descricao, "valor": valor})
    salvar_gastos(gastos)
    return True


def calcular_total():
    gastos = carregar_gastos()
    return sum(item['valor'] for item in gastos)


def menu():
    while True:
        print(f"\n=== GERENCIADOR DE GASTOS v{__version__}===")
        print("1. Adicionar Novo Gasto")
        print("2. Listar Todos os Gastos")
        print("3. Exibir Total Acumulado")
        print("4. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            desc = input("Descrição do gasto: ")
            try:
                val = float(input("Valor (ex: 50.25): R$ "))
                adicionar_gasto(desc, val)
                print(" Gasto registrado!")
            except ValueError as e:
                print(f" Erro: {e}")
        elif opcao == '2':
            gastos = carregar_gastos()
            print("\n--- LISTA DE GASTOS ---")
            if not gastos: 
                print("Nenhum gasto registrado.")
            for g in gastos:
                print(f"• {g['descricao']}: R$ {g['valor']:.2f}")
        elif opcao == '3':
            print(f"\n TOTAL GERAL: R$ {calcular_total():.2f}")
        elif opcao == '4':
            print("Encerrando...")
            break
        else:
            print(" Opção inválida.")


if __name__ == "__main__":
    menu()
