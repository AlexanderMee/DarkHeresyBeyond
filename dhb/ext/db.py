import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(parent_dir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Import your SQLAlchemy models into the Flask app
    from ..models import User

    #initialise app
    db.init_app(app)

    # Create the database tables (must go after app is initalised!)
    with app.app_context():
        db.create_all()

