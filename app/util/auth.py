import jwt
from functools import wraps
from flask import current_app, request
from app.models.user import User

def jwt_required(f):
    wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return {'Erro': 'Essa rota necessita de um token :/'}
        
        if not 'JWT' in token:
            return {'Erro': 'Token Invalido'}
        
        try:
            token_puro = token.replace('JWT ','')
            decoded = jwt.decode(token_puro, current_app.config.get("SECRET_KEY"), algorithms="HS256")
            current_user = User.query.get(decoded['id'])
        except:
            return {'Erro': 'Token Invalido'}

        

        return f(*args, **kwargs)
    
    return wrapper
