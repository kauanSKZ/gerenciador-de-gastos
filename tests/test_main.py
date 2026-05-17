from unittest.mock import patch
import pytest
import os
import src.main as app
from src.main import obter_cotacao_dolar


@patch("src.main.requests.get")
def test_integracao_api_cotacao(mock_get):
    """Testa se a aplicação consegue lidar com a chamada de cotação."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"USDBRL": {"bid": "5.10"}}

    cotacao = obter_cotacao_dolar()

    assert cotacao is not None
    assert isinstance(cotacao, float)
    assert cotacao > 0


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
