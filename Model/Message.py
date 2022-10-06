'''Schema:'''
from app_module import db, ma

class Message(db.Model):
    __tablename__= 'tbl_message'
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    messagem = db.Column(db.String(2500), nullable = False, unique = False)
    created_date = db.Column(db.DateTime, nullable = False)

class Message_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
