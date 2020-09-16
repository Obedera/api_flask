from flask import Blueprint
from flask_restplus import Api
from werkzeug.utils import cached_property

from app.controllers.cliente.cliente import api as ns_cliente
from app.controllers.login.login import api as ns_user

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    api_bp,
    version="1.0",
    title="Flask API Blocks",
    description="Swagger UI documentation Api Blocks!",
    doc="/ui",
)

api.add_namespace(ns_cliente, path="/cliente")
api.add_namespace(ns_user, path="/login")