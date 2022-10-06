'''Controller para módulo de fale conosco'''
from email import message
from flask import request
from flask import jsonify
from app_module import create_app, db
from Model.Message import Message, Message_Schema
from datetime import datetime

app = create_app()
app.app_context().push()

message_Schema = Message_Schema()
messages_Schema = Message_Schema(many = True)

def home():
    '''Mensagem de boas vindas'''
    return jsonify("Olá, bem vindo ao SAC do E-commerce.com!"), 200

def index():
    '''Retorna todas as mensagens da API:'''
    messages = Message.query.order_by(Message.created_date).all()
    return jsonify(messages_Schema.dump(messages)), 200

    
def create():
    if request.is_json:
        m = request.get_json()

        message = Message(
            usuario = m['usuario'],
            email = m['email'],
            messagem = m['messagem'],
            created_date = datetime.now()
        )
        db.session.add(message)
        db.session.commit()

    return "O E-commerce.com agradece o seu contato!", 201

