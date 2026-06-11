import pytest
# Importa o app. Ajuste o caminho se o arquivo principal estiver em outra subpasta
from task_manager_flask import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_pagina_inicial(client):
    rv = client.get('/')
    assert rv.status_code == 200