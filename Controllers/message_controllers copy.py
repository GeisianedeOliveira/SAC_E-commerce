'''Controller para módulo de fale conosco'''
from flask import request
from flask import jsonify
from app_module import create_app, db
from Model.banco_de_dados import Message, Message_Schema

app = create_app()
app.app_context().push()

message_Schema = Message_Schema()
messages_Schema = Message_Schema(Many = True)

def index():
    """Lista de mensagens:"""
    messages = Message.query.filter(not Message.deleted).order_by(Message.create_date).all()
    return jsonify(messages_Schema.dump(Message)), 200

def create():
    if request.is_json:
        m = request.get()

        message = Message(
            usuario = m['usuario'],
            email = m['email'],
            messagem = m['messagem']
        )
        db.session.add(message)
        db.session.commit()
    
        return 201



def read(id):
    """Lista de mensagens por ID:"""
    message = Message.query.filter_by(id = id).first()
    return message_Schema.jsonify(Message), 200


