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
def test_listar_marcadores_unidade(client, id_unidade):
    marcadores = client.listar_marcadores_unidade(id_unidade)

    assert marcadores[0].id_marcador != ""
    assert marcadores[0].nome != ""
    assert marcadores[0].icone != ""


@pytest.mark.integration
def test_listar_series(client):
    series = client.listar_series()
    if len(series) > 0:
        assert series[0].id_serie != ""
        assert series[0].nome != ""
        if series[0].aplicabilidade is not None:
            assert isinstance(series[0].aplicabilidade, Aplicabilidade)


@pytest.mark.integration
def test_consultar_documento(client, id_unidade, protocolo_documento):
    if id_unidade is None or protocolo_documento is None:
        pytest.skip("id_unidade ou procotolo_documento não definidos")

    documento = client.consultar_documento(
        id_unidade=id_unidade,
        protocolo_documento=protocolo_documento,
    )

    assert documento.id_documento != ""
    assert documento.procedimento_formatado != ""
    assert documento.documento_formatado == protocolo_documento


@pytest.mark.integration
def test_consultar_procedimento(client, id_unidade, protocolo_procedimento):
    if id_unidade is None or protocolo_procedimento is None:
        pytest.skip("id_unidade ou protocolo_procedimento não definidos")

    procedimento = client.consultar_procedimento(
        id_unidade=id_unidade,
        protocolo_procedimento=protocolo_procedimento,
        retornar_andamento_geracao=True,
    )

    assert procedimento.id_procedimento != ""
    assert procedimento.procedimento_formatado == protocolo_procedimento
