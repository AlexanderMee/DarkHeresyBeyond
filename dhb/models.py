from .ext.db import db #from current module/ext/db import the variable db (sqlalchemy)

from flask_login import UserMixin
from datetime import datetime

#user table
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    profile_pic = db.Column(db.String, nullable=False)

    @staticmethod
    def get(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create(id_, name, email, profile_pic):
        user = User(id=id_, name=name, email=email, profile_pic=profile_pic)
        db.session.add(user)
        db.session.commit()
        return user
    
    def __repr__(self):
        return f"<User {self.id}: {self.name}>"

    
#character table
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Character {self.id}: {self.name}>"
