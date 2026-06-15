from src.database import supabase


def obter_cotacao_dolar():
    try:
        pass
    except Exception:
        pass


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
        print("===================================\n")

    except Exception as e:
        print(f"Erro ao buscar gastos: {e}")


def filtrar_gastos_altos(valor_limite: float):
    try:
        resposta = supabase.table("gastos").select("*").gt(
            "valor", valor_limite
        ).execute()
        gastos_filtrados = resposta.data

        if not gastos_filtrados:
            print(f"Nenhum gasto cadastrado acima de R$ {valor_limite:.2f}")
            return

        print(f"\n--- GASTOS ACIMA DE R$ {valor_limite:.2f} ---")
        for g in gastos_filtrados:
            print(f"- {g['descricao']}: R$ {g['valor']:.2f}")

    except Exception as e:
        print(f"Erro ao filtrar dados: {e}")


def exibir_menu():
    print("\n=== GERENCIADOR DE GASTOS ===")
    print("1. Cadastrar Gasto")
    print("2. Listar Gastos")
    print("3. Filtrar Gastos Altos")
    print("0. Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Funcionalidade de cadastro gerenciada pela Issue #4.")
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            try:
                limite_txt = input("Exibir gastos maiores que quanto (R$)? ")
                limite = float(limite_txt)
                filtrar_gastos_altos(limite)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
