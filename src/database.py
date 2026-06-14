import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise ValueError(
        "Erro: As variáveis de ambiente SUPABASE_URL e SUPABASE_KEY "
        "não foram encontradas no arquivo .env!"
    )

supabase: Client = create_client(url, key)
print("Conexão com o Supabase configurada com sucesso!")


def criar_gasto(descricao: str, valor: float):
    """
    Insere um novo gasto na tabela 'gastos' do Supabase.
    """
    try:
        dados = {
            "descricao": descricao,
            "valor": valor
        }
        resposta = supabase.table("gastos").insert(dados).execute()
        print("\nGasto salvo com sucesso no banco de dados!")
        return resposta.data
    except Exception as e:
        print(f"\nErro ao salvar gasto no Supabase: {e}")
        return None