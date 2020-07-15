import os 

class Config:
    '''
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProductionConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')

class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}