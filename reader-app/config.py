import os
import secrets


class Config(object):
    NAME = 'File Reader App'

    TESTING = False
    DEBUG = True

    # App version
    VERSION = '1.0'

    # static files folder
    STATIC_FOLDER = 'static'

    # file upload settings
    MAX_CONTENT_LENGTH = 25 * 1024 * 1024


class Development(Config):
    # Enabling the development environment
    FLASK_CONFIG = 'development'

    # Secret key for signing cookies
    SECRET_KEY = 'development'


class Production(Config):
    # Enabling the production environment
    FLASK_CONFIG = 'production'

    DEBUG = False

    # Secret key for signing cookies
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_urlsafe(32))


class Testing(Config):
    # Enabling the testing environment
    FLASK_CONFIG = 'testing'

    TESTING = True

    # Secret key for signing cookies
    SECRET_KEY = 'testing'
