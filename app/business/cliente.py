from flask import jsonify
from app.models.cliente import Cliente
from app import db




def add_cliente(data):
    try:
        cliente = Cliente(
            celular=data.get('celular'),
            cpf=data.get('cpf'),
            data_nascimento=data.get('data_nascimento'),
            email=data.get('email'),
            nome=data.get('nome')
            )
        salvar_bd(cliente)
        return {
            'msg':"Cliente Criado com Sucesso",
        }, 202
    except:
        return {
            'msg':"Cliente já Existe"
        }, 404
        

def get_all_clientes():
    return Cliente.query.all() 

def get_cliente(id):
    return Cliente.query.filter(Cliente.id == id).one()

def put_cliente(id,data):
    try:
        cliente = get_cliente(id)
        cliente.celular=data.get('celular'),
        cliente.cpf=data.get('cpf'),
        cliente.data_nascimento=data.get('data_nascimento'),
        cliente.email=data.get('email'),
        cliente.nome=data.get('nome')
        db.session.commit()
        return {
            'msg':"Cliente Atualizado com Sucesso",
        }, 202
    except:
        return {
            'msg':"Cliente Não Existe"
        }, 404

def delete_cliente(id):
    try:
        remover_bd(get_cliente(id))
        return {
            'msg':"Cliente Removido com Sucesso",
        }, 202
    except:
        return {
            'msg':"Cliente Não Existe"
        }, 404



def salvar_bd(data):
    db.session.add(data)
    db.session.commit()

def remover_bd(data):
    db.session.delete(data)
    db.session.commit()