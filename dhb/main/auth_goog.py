from flask import Blueprint

auth_goog = Blueprint('auth_goog', __name__)

@auth_goog.route('/login')
def login():
    return 'Login page'

@auth_goog.route('/register')
def register():
    return 'Register page'