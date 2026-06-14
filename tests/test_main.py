from unittest.mock import patch, MagicMock
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


@patch("src.main.supabase")
def test_caminho_feliz_adicionar_gasto(mock_supabase):
    mock_execute = MagicMock()
    mock_supabase.table.return_value.insert.return_value.execute.return_value = (
        mock_execute
    )

    assert app.adicionar_gasto("Internet", 100.0) is True
    mock_supabase.table.assert_called_with("gastos")
    mock_supabase.table.return_value.insert.assert_called_with(
        {"descricao": "Internet", "valor": 100.0}
    )


def test_entrada_invalida_valor_negativo():
    with pytest.raises(ValueError, match="O valor deve ser maior que zero"):
        app.adicionar_gasto("Erro", -50.0)


@patch("src.main.supabase")
def test_caso_limite_soma_vazia(mock_supabase):
    mock_response = MagicMock()
    mock_response.data = []
    mock_supabase.table.return_value.select.return_value.execute.return_value = (
        mock_response
    )

    assert app.calcular_total() == 0