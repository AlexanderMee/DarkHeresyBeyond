#Flask
from flask import Flask

#Extentions, each extention should have its own file in extentions folder
from .config import config 
from .ext import db, loginManager, oauth
from .ext.oauth import google
#from .main.auth_goog import auth_goog
from .main.index import index
from .main.test import test

#create_app is a custom function, by convention called create_app, it initalises flask, extentions, config, blueprints, the order is important!
def create_app():
    app = Flask(__name__)

    #config set up
    app.config.from_object(config)
    config.init_app(app)

    #database setup
    db.init_app(app)

    #other extentions
    loginManager.init_app(app)
    #google = oauth.init_app(app)
    #print("this is google:{}".format(google))

    #blueprints
    app.register_blueprint(index)
    app.register_blueprint(test)       
    #.register_blueprint(auth_goog)
        
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///db.sqllite3'

    return app
