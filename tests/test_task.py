import sys
import os
import pytest

# Garante que a raiz do projeto e a pasta todo_project estão no PATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
