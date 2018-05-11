import os


class Config:
    DEBUG = True

    # Alphabet without similar characters 1, I, l, 0 and O
    # without meaningful words (a, e, i, o and u removed)
    ALPHABET = "23456789bcdfghjkmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ-_"
    EXCLUDED_CHARACTERS = {'a', 'e', 'i', 'o', 'u', '1', 'I', 'l', 'O', '0'}

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    # ********** DATABASE ***********************
    DB_USER = 'admin'
    DB_PASSWORD = 'admin'
    DB_HOST = 'localhost'
    DB_NAME = 'test_api'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

    # ********** TESTING ************************
    TESTING = False


class LocalConfig(Config):
    """ Umbrella config for all local runs,
     vagrant runs and unit testing runs """
    BASE_URL = 'http://localhost:5000/'


class ProductionConfig(Config):
    """ Config used in production environment """
    DEBUG = False


config = {
    'local': LocalConfig,
    'production': ProductionConfig
}

SELECTED_CONFIG = os.getenv('API_ENV', 'local')