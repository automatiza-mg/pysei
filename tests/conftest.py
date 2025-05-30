from os import environ

import pytest
from dotenv import load_dotenv

from python_sei import Client

load_dotenv()


@pytest.fixture
def client():
    url = environ.get("SEI_URL")
    sigla_sistema = environ.get("SEI_SIGLA_SISTEMA")
    identificacao_servico = environ.get("SEI_IDENTIFICACAO_SERVICO")

    return Client(url, sigla_sistema, identificacao_servico)


@pytest.fixture
def id_unidade():
    return environ.get("TEST_ID_UNIDADE")


@pytest.fixture
def protocolo_documento():
    return environ.get("TEST_PROTOCOLO_DOCUMENTO")


@pytest.fixture
def protocolo_procedimento():
    return environ.get("TEST_PROTOCOLO_PROCEDIMENTO")
