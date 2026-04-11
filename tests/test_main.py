import pytest
import os
from src.main import carregar_gastos, salvar_gastos


@pytest.fixture(autouse=True)
def gerenciar_arquivo_teste():
    if os.path.exists('gastos.json'):
        os.remove('gastos.json')
    yield
    if os.path.exists('gastos.json'):
        os.remove('gastos.json')


def test_lista_vazia_ao_iniciar():
    gastos = carregar_gastos()
    assert len(gastos) == 0


def test_adicionar_e_carregar_gasto():
    dados = [{"descricao": "Teste", "valor": 10.0}]
    salvar_gastos(dados)
    carregados = carregar_gastos()
    assert carregados[0]["descricao"] == "Teste"