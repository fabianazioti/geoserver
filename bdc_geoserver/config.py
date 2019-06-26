import os


def get_settings(env):
    return eval(env)


class Config():
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    SECRET_KEY = os.environ.get('KEYSYSTEM', 'bdc_geoserver')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ.get('POSTGRES_USER'), os.environ.get('POSTGRES_PASSWORD'), os.environ.get('POSTGRES_HOST'),
        os.environ.get('POSTGRES_PORT'), os.environ.get('POSTGRES_DATABASE'))


class ProductionConfig(Config):
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True


key = Config.SECRET_KEY

