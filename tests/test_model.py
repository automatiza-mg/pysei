from python_sei.models import Unidade


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

    assert unidades[1].id_unidade == "110001135"
    assert unidades[1].sigla == "SES/URSTOF-NUVISA"
    assert unidades[1].descricao == "Vigilancia Sanitária Teófilo Otoni"
    assert unidades[1].protocolo
    assert not unidades[1].arquivamento
    assert not unidades[1].ouvidoria
