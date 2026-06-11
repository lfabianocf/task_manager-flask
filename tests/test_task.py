import sys
import os
import pytest

# Garante que a raiz do projeto (task_manager-flask) está no PATH do Python
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Força a variável de ambiente de teste para o __init__.py ler
os.environ['FLASK_ENV'] = 'testing'

# Importa o app e o db do arquivo run.py que está dentro de todo_project
from todo_project import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    
    # Cria o contexto do banco de dados antes do teste se necessário
    with app.app_context():
        if 'db' in globals():
            db.create_all()
            
    with app.test_client() as client:
        yield client
        
    # Limpa o banco após a execução do teste
    with app.app_context():
        if 'db' in globals():
            db.drop_all()

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
