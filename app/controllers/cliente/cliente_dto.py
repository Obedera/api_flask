from flask_restplus import Namespace
from flask_restplus.fields import String, Integer, DateTime


class Cliente_DTO:
    ns_cliente = Namespace('cliente', validate=True)

    cliente_dto = ns_cliente.model('Cliente',{
        "id": Integer,
        "nome": String(required=True, description='nome do cliente'),
        "cpf":String(required=True),
        "celular":String,
        "email": String(required=True),
        "data_nascimento": DateTime
    })