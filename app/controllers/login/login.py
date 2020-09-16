from flask import request
from flask_restplus import Resource
from app.business.login import add_user_login, get_all_users, get_user_login, login_user
from app.controllers.login.login_dto import User_DTO
from app.util.auth import jwt_required


api = User_DTO.ns_user
_login_dto = User_DTO.login_dto
_user_dto = User_DTO.user_dto
_recuperar_dto = User_DTO.recuperar_dto

@api.route('/cadastrar')
class UserCadastrar(Resource):
    
    @api.expect(_user_dto, validate=True)
    def post(self):
        request_data = request.json
        return add_user_login(request_data)

@api.route('/')
class UserLista(Resource):
    @api.expect(_login_dto, validate=True)
    def post(self):
        request_data = request.json
        return login_user(request_data)

    @jwt_required
    @api.marshal_list_with(_user_dto, envelope='data')
    def get(self):
        return get_all_users()
    



@api.route('/<int:id>')
@api.doc(params={'id': 'id User'})
class User(Resource):

    @api.marshal_with(_user_dto)
    def get(self, id):
        try:
            user = get_user_login(id)
            return user
        except:
            return api.abort(404,message='User não encontrado!!')    
