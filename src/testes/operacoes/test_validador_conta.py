import pytest
from tech.robertobzrr.operacoes.validador_conta import validar_abertura_conta


def test_cenario_caminho_feliz_aprovado():
    resultado = validar_abertura_conta(25, 700)
    assert resultado == "Conta aprovada."


def test_cenario_idade_invalida():
    with pytest.raises(ValueError) as excinfo:
        validar_abertura_conta(16, 700)
    assert str(excinfo.value) == "Idade inválida."
    

def test_cenario_score_insuficiente():
    resultado = validar_abertura_conta(25, 400)
    assert resultado == "Score Insuficiente."

