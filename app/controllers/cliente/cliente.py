from flask import request
from flask_restplus import Resource
from app.business.cliente import add_cliente, get_cliente, get_all_clientes, put_cliente, delete_cliente
from app.controllers.cliente.cliente_dto import Cliente_DTO


api = Cliente_DTO.ns_cliente
_dto = Cliente_DTO.cliente_dto

@api.route('/')
class ClienteLista(Resource):

    @api.marshal_list_with(_dto, envelope='data')
    def get(self):
        return get_all_clientes()

    @api.expect(_dto, validate=True)
    def post(self):
        request_data = request.json
        return add_cliente(request_data)



@api.route('/<int:id>')
@api.doc(params={'id': 'id do Cliente'})
class Cliente(Resource):    


    @api.marshal_with(_dto)
    def get(self, id):
        try:
            cliente = get_cliente(id)
            return cliente    
        except:
            return api.abort(404,message='Cliente não encontrado!!')

    @api.expect(_dto, validate=True)
    def put(self, id):
        return put_cliente(id,request.json)
    
    def delete(self, id):
        return delete_cliente(id)