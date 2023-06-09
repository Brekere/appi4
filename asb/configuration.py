class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key5&6423v-daD2?s'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://asbsistemas:asbsistemas@192.168.0.12:3306/app4_0"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret!'
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'