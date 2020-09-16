from flask_restplus import Namespace
from flask_restplus.fields import String, Integer


class User_DTO:
    ns_user = Namespace('user', validate=True)

    login_dto = ns_user.model('User Login',{
        "username": String(required=True),
        "password": String(required=True),
    })

    user_dto = ns_user.model('User Cadastro',{
        "id": Integer,
        "username": String(required=True),
        "email":String(required=True),
        "password": String(required=True),
    })

    recuperar_dto = ns_user.model('User Recuperar',{
        "email":String(required=True),
    })