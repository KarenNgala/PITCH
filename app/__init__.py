from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    #init
    db.init_app(app)

    #set up
    app.config.from_object(config_options[config_name])

    #reg
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app