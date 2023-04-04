from flask import Blueprint

test = Blueprint('test', __name__)

@test.route('/test')
def login():
    return 'Login Page'