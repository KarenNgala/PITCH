from flask import Flask
from config import DevelopmentConfig

#init
app = Flask(__name__)

#set up
app.config.from_object(DevelopmentConfig)

from app import views