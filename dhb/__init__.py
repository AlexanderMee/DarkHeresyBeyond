#Flask
from flask import Flask

#Extentions, each extention should have its own file in extentions folder
from .ext import db

#create_app is a custom function, by convention called create_app, it initalises flask, extentions, config, blueprints
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///db.sqllite3'
    return app
