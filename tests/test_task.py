import sys
import os
import pytest

# 1. Encontra a pasta pai 'todo_project' dentro da raiz
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TODO_PAI = os.path.join(ROOT_DIR, 'todo_project')

# 2. Injeta essa pasta pai no PATH do Python
if TODO_PAI not in sys.path:
    sys.path.insert(0, TODO_PAI)

os.environ['FLASK_ENV'] = 'testing'

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
