from flask import Blueprint
from flask_login import current_user

index = Blueprint('index', __name__)

@index.route('/')
def hello(): #can not be the same name as the blueprint name
    if current_user.is_authenticated:
        return f"Hello {current_user.name}"
    else:
        return "Hello stranger"

@index.route('/hi')
def hi(): #can not be the same name as the blueprint name
    return 'Hi World!'

@index.route('/salut')
def salut(): #can not be the same name as the blueprint name
    return 'Bonjour tous le monde!'
