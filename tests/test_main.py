from unittest.mock import MagicMock, patch
from src.main import filtrar_gastos_altos, listar_gastos


@patch("src.main.supabase")
def test_listar_gastos_com_sucesso(mock_supabase):
    mock_response = MagicMock()
    mock_response.data = [
        {"id": 1, "descricao": "Almoço", "valor": 35.50},
        {"id": 2, "descricao": "Internet", "valor": 100.00}
    ]
    mock_select = mock_supabase.table.return_value.select.return_value
    mock_select.execute.return_value = mock_response

    listar_gastos()
    mock_supabase.table.assert_called_with("gastos")


@patch("src.main.supabase")
def test_listar_gastos_vazio(mock_supabase):
    mock_response = MagicMock()
    mock_response.data = []
    mock_select = mock_supabase.table.return_value.select.return_value
    mock_select.execute.return_value = mock_response

    listar_gastos()
    mock_supabase.table.assert_called_with("gastos")


@patch("src.main.supabase")
def test_filtrar_gastos_altos_com_sucesso(mock_supabase):
    mock_response = MagicMock()
    mock_response.data = [
        {"id": 2, "descricao": "Internet", "valor": 100.00}
    ]
    mock_chain = mock_supabase.table.return_value.select.return_value.gt
    mock_chain.return_value.execute.return_value = mock_response

    filtrar_gastos_altos(50.00)
    mock_supabase.table.assert_called_with("gastos")


@patch("src.main.supabase")
def test_filtrar_gastos_altos_vazio(mock_supabase):
    mock_response = MagicMock()
    mock_response.data = []
    mock_chain = mock_supabase.table.return_value.select.return_value.gt
    mock_chain.return_value.execute.return_value = mock_response

    filtrar_gastos_altos(200.00)
    mock_supabase.table.assert_called_with("gastos")
