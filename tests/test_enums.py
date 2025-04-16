from python_sei.enums import NivelAcesso


def test_nivel_acesso_from_str():
    assert NivelAcesso.from_str("0") == NivelAcesso.PUBLICO
    assert NivelAcesso.from_str("1") == NivelAcesso.RESTRITO
    assert NivelAcesso.from_str("2") == NivelAcesso.SIGILOSO


def test_nivel_acesso_to_str():
    assert NivelAcesso.PUBLICO.to_str() == "0"
    assert NivelAcesso.RESTRITO.to_str() == "1"
    assert NivelAcesso.SIGILOSO.to_str() == "2"
