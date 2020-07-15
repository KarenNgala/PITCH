import os 

class Config:
    '''
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    UPLOADED_PHOTOS_DEST='app/static/photos'

class ProductionConfig(Config):
    '''
    '''
    pass

class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}