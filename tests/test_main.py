from src.main import obter_cotacao_dolar


def test_integracao_api_cotacao():
    """Testa se a aplicação consegue se comunicar com a API de cotação."""
    cotacao = obter_cotacao_dolar()
    
    assert cotacao is not None
    assert isinstance(cotacao, float)
    assert cotacao >0


import pytest
import os
import src.main as app


@pytest.fixture(autouse=True)
def gerenciar_arquivo_teste():
    app.ARQUIVO_DADOS = "test_gastos.json"
    if os.path.exists("test_gastos.json"):
        os.remove("test_gastos.json")
    yield
    if os.path.exists("test_gastos.json"):
        os.remove("test_gastos.json")


def test_caminho_feliz_adicionar_gasto():
    assert app.adicionar_gasto("Internet", 100.0) is True
    assert len(app.carregar_gastos()) == 1


def test_entrada_invalida_valor_negativo():
    with pytest.raises(ValueError, match="O valor deve ser maior que zero"):
        app.adicionar_gasto("Erro", -50.0)


def test_caso_limite_soma_vazia():
    assert app.calcular_total() == 0
