from os import environ

import pytest
from dotenv import load_dotenv

from pysei import Client

load_dotenv()


@pytest.fixture
def client():
    url = environ.get("SEI_URL")
    sigla_sistema = environ.get("SEI_SIGLA_SISTEMA")
    identificacao_servico = environ.get("SEI_IDENTIFICACAO_SERVICO")

    return Client(url, sigla_sistema, identificacao_servico)
