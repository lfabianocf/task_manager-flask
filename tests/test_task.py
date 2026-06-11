import sys
import os
import pytest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 2. Insere a raiz no PATH do Python se ela já não estiver lá
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
# Se dentro de todo_project você tem o arquivo app.py:

try:
    from todo_project.app import app
except ModuleNotFoundError:
    # Caso o todo_project já seja o próprio pacote
    from todo_project import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_task_exists():
    assert app is not None

def test_pagina_inicial(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_login(client):
    rv = client.get('/login')
    assert rv.status_code == 200

def test_registro(client):
    rv = client.get('/register')
    assert rv.status_code == 200
