import jwt
from app import db
from datetime import datetime, timedelta
from flask import current_app

class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(84), nullable=False, unique=True)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(84), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))
    data_atualizacao = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0), onupdate=datetime.now().replace(microsecond=0))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = f'{password}'

    # def verify_password(self, password):
    #     return check_password_hash(self.password, password)

    def encode_access_token(self):
        now = datetime.utcnow()
        token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
        token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
        expire = now + timedelta(hours=token_age_h, minutes=token_age_m)
        payload = dict(exp=expire, iat=now, id=self.id)
        key = current_app.config.get("SECRET_KEY")
        return jwt.encode(payload, key, algorithm="HS256")