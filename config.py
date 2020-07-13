import os 

class Config:
    '''
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')

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