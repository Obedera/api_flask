import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()




def create_app(config_name):
    app = Flask(__name__)


    app.config.from_object(get_config(config_name))

    from app.controllers import api_bp

    app.register_blueprint(api_bp)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


    return app