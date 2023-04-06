from .ext.db import db #from current module/ext/db import the variable db (sqlalchemy)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    profile_pic = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    