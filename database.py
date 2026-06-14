import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Erro: As variáveis de ambiente SUPABASE_URL e SUPABASE_KEY não foram encontradas no arquivo .env!")

supabase: Client = create_client(url, key)
print("Conexão com o Supabase configurada com sucesso!")