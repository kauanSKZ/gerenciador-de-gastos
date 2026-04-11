import pytest
import os
import src.main as app


@pytest.fixture(autouse=True)
def gerenciar_arquivo_teste():
    """Configura arquivo de teste e limpa após o uso."""
    app.ARQUIVO_DADOS = "test_gastos.json"
    if os.path.exists("test_gastos.json"):
        os.remove("test_gastos.json")
    yield
    if os.path.exists("test_gastos.json"):
        os.remove("test_gastos.json")



def test_caminho_feliz_adicionar_gasto():
    """Teste 1: Adição correta de um gasto."""
    assert app.adicionar_gasto("Internet", 100.0) is True
    assert len(app.carregar_gastos()) == 1



def test_entrada_invalida_valor_negativo():
    """Teste 2: Validação de erro para valor negativo."""
    with pytest.raises(ValueError, match="O valor deve ser maior que zero"):
        app.adicionar_gasto("Erro", -50.0)



def test_caso_limite_soma_vazia():
    """Teste 3: Verificação do total quando não há gastos."""
    assert app.calcular_total() == 0
