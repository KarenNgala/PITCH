import os 

class Config:
    '''
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://lalu:0@localhost/pitch'

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