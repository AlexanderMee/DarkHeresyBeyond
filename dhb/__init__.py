#Flask
from flask import Flask

#Extentions, each extention should have its own file in extentions folder
from .config import config 
from .ext import db, loginManager, oauth, bootstrap, wtf
from .main.auth_goog import auth_goog
from .main.index import index
from .main.characters import characters_bp


#create_app is a custom function, by convention called create_app, it initalises flask, extentions, config, blueprints, the order is important!
def create_app():
    app = Flask(__name__)

    #config set up
    app.config.from_object(config)
    config.init_app(app)

    #database setup
    db.init_app(app)
    #import model, must occur after db initalised 
    from .models import User
    #create db tables, must occur after model import
    with app.app_context():
        db.db.create_all() #note db.db, this accesses the database db, not the extention 

    #google config, create google data model for api access, this is saved to config file so it can be accessed across files (i.e. by auth_goog)
    google = oauth.init_app(app)
    app.config['google'] = google
  
    #other extentions
    loginManager.init_app(app)
    bootstrap.init_app(app)
    #wtf.init_app(app)

    #blueprints
    app.register_blueprint(index)  
    app.register_blueprint(auth_goog)
    app.register_blueprint(characters_bp)

    return app