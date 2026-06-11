import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '45cf93c4d41348cd9980674ade9a7356'


# Se o arquivo de teste injetar 'TESTING = True', usamos um banco em memória
if os.environ.get('FLASK_ENV') == 'testing' or app.config.get('TESTING'):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
else:
    # Caminho padrão para quando rodar dentro do Docker
    INSTANCE_DIR = "/app/data"
    # Garante que a pasta existe (evita erros de diretório ausente)
    os.makedirs(INSTANCE_DIR, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(INSTANCE_DIR, "site.db")

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# IMPORTAR ROTAS NO FINAL (DEPOIS DO APP EXISTIR)
from todo_project import routes  # noqa: E402,F401
# from . import routes  # noqa: E402,F401
