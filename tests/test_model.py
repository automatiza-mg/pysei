from python_sei.models import Unidade, Usuario, Serie
from python_sei.enums import Aplicabilidade


def test_unidade():
    records = [
        {
            "IdUnidade": "110001133",
            "Sigla": "SES/URSSJD-NUVISA",
            "Descricao": "Vigilancia Sanitária São João Del Rei",
            "SinProtocolo": "N",
            "SinArquivamento": "S",
            "SinOuvidoria": "S",
        },
        {
            "IdUnidade": "110001135",
            "Sigla": "SES/URSTOF-NUVISA",
            "Descricao": "Vigilancia Sanitária Teófilo Otoni",
            "SinProtocolo": "S",
            "SinArquivamento": "N",
            "SinOuvidoria": "N",
        },
    ]

    unidades = Unidade.from_many_records(records)

    assert len(unidades) == 2

    assert unidades[0].id_unidade == "110001133"
    assert unidades[0].sigla == "SES/URSSJD-NUVISA"
    assert unidades[0].descricao == "Vigilancia Sanitária São João Del Rei"
    assert not unidades[0].protocolo
    assert unidades[0].arquivamento
    assert unidades[0].ouvidoria
    assert unidades[0].raw_value == records[0]

    assert unidades[1].id_unidade == "110001135"
    assert unidades[1].sigla == "SES/URSTOF-NUVISA"
    assert unidades[1].descricao == "Vigilancia Sanitária Teófilo Otoni"
    assert unidades[1].protocolo
    assert not unidades[1].arquivamento
    assert not unidades[1].ouvidoria
    assert unidades[1].raw_value == records[1]


def test_usuario():
    records = [
        {
            "IdUsuario": "100000293",
            "Sigla": "teste_externo",
            "Nome": "Teste Usuário Externo",
        }
    ]

    usuarios = Usuario.from_many_records(records)

    assert len(usuarios) == 1
    assert usuarios[0].id_usuario == "100000293"
    assert usuarios[0].sigla == "teste_externo"
    assert usuarios[0].nome == "Teste Usuário Externo"
    assert usuarios[0].raw_value == records[0]


def test_serie():
    records = [
        {
            "IdSerie": "491",
            "Nome": "Processo",
            "Aplicabilidade": "T",
        },
        {
            "IdSerie": "722",
            "Nome": "Processo Administrativo Sigiloso",
            "Aplicabilidade": "E",
        },
        {
            "IdSerie": "339",
            "Nome": "Procuração",
            "Aplicabilidade": "T",
        },
    ]

    series = Serie.from_many_records(records)

    assert len(series) == 3

    assert series[0].id_serie == "491"
    assert series[0].nome == "Processo"
    assert series[0].aplicabilidade == Aplicabilidade.DOCUMENTOS_INTERNOS_EXTERNOS
    assert series[0].raw_value == records[0]

    assert series[1].id_serie == "722"
    assert series[1].nome == "Processo Administrativo Sigiloso"
    assert series[1].aplicabilidade == Aplicabilidade.DOCUMENTOS_EXTERNOS
    assert series[1].raw_value == records[1]

    assert series[2].id_serie == "339"
    assert series[2].nome == "Procuração"
    assert series[2].aplicabilidade == Aplicabilidade.DOCUMENTOS_INTERNOS_EXTERNOS
    assert series[2].raw_value == records[2]
