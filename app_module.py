'''Inicia e disponibiliza o módulo APP para ser utilizado ao longo de toda a aplicação'''

from flask import Flask
import utils.config
from utils.db_init import db, ma

def create_app():
    '''Função que inicializa os módulos para funcionar o projeto com banco de dados'''
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = utils.config.DATABASE_CONN
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    
    return app