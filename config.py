import os 

class Config:
    '''
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')

class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True

class ProductionConfig(Config):
    '''
    '''
    pass

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}