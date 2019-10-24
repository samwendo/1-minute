import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:54321@localhost/ti'
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''


class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:54321@localhost/ti_test'

    DEBUG = True

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:54321@localhost/ti'
    
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")

    


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
