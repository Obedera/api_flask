from flask import jsonify
from app.models.user import User
from app import db


def login_user(data):
    user = User.query.filter_by(username=data.get('username'), password=data.get('password')).first()
    if user is not None:
        print(user)
        token = user.encode_access_token()
        print(token)
        return {
            'msg':'Sucesso',
            'auth':True,
            'token': token.decode()
        }, 200
    return {
        'msg': 'Error'
    }, 403


def add_user_login(data):
    try:
        user = User(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
            )
        salvar_bd(user)
        return {
            'msg':"Login Criado com Sucesso",
        }, 202
    except:
        return {
            'msg':"Login já Existe"
        }, 404
        

def get_all_users():
    return User.query.all() 

def get_user_login(id):
    return User.query.filter(User.id == id).one()


def salvar_bd(data):
    db.session.add(data)
    db.session.commit()

def remover_bd(data):
    db.session.delete(data)
    db.session.commit()