from datetime import datetime
from app import db

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    celular = db.Column(db.String(14))
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    nome = db.Column(db.String(128))
    data_nascimento = db.Column(db.DateTime)
    data_criacao = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))
    data_atualizacao = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0), onupdate=datetime.now().replace(microsecond=0))