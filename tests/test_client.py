import pytest
from python_sei.enums import Aplicabilidade


@pytest.mark.integration
def test_listar_unidades(client):
    unidades = client.listar_unidades()
    if len(unidades) > 0:
        assert unidades[0].id_unidade != ""


@pytest.mark.integration
def test_listar_usuarios(client):
    unidades = client.listar_unidades()
    for unidade in unidades:
        usuarios = client.listar_usuarios(unidade.id_unidade)
        if len(usuarios) == 0:
            continue

        assert usuarios[0].id_usuario != ""
        assert usuarios[0].nome != ""
        assert usuarios[0].sigla != ""
        break


@pytest.mark.integration
@pytest.mark.skip(reason="O endpoint retorna um erro interno")
def test_listar_marcadores_unidade(client):
    unidades = client.listar_unidades()
    for unidade in unidades:
        marcadores = client.listar_marcadores_unidade(unidade.id_unidade)
        if len(marcadores) == 0:
            continue

        assert marcadores[0].id_marcador != ""
        assert marcadores[0].nome != ""
        assert marcadores[0].icone != ""
        break


@pytest.mark.integration
def test_listar_series(client):
    series = client.listar_series()
    if len(series) > 0:
        assert series[0].id_serie != ""
        assert series[0].nome != ""
        if series[0].aplicabilidade is not None:
            assert isinstance(series[0].aplicabilidade, Aplicabilidade)
