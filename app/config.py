import os
from pathlib import Path


APP_ROOT = Path(__file__).parent
user = os.getenv('RDS_USERNAME')
pw = os.getenv('RDS_PASSWORD')
url = os.getenv('RDS_HOSTNAME')
db = os.getenv('RDS_DB_NAME')
DB_HOST = f'postgresql://{user}:{pw}@{url}/{db}'
DB_TEST = "sqlite:///" + str(APP_ROOT / "bd_prod.sqlite")


class Config:
    """Base configuration."""
    ORIGINS = ["*"]

    SECRET_KEY = '\xe38\xf7\xea\x1bK\xa5UZ\x95\xd9\x9b\x8f\x1a \x93'
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = DB_HOST

class DevelopmentConfig(Config):
    """Development configuration."""

    TOKEN_EXPIRE_MINUTES = 15


class ProductionConfig(Config):
    """Production configuration."""

    TOKEN_EXPIRE_HOURS = 1
    BCRYPT_LOG_ROUNDS = 13
    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig, production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)