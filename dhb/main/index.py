from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/hello')
def hello(): #can not be the same name as the blueprint name
    return 'Hello World!'

@index.route('/hi')
def hi(): #can not be the same name as the blueprint name
    return 'Hi World!'

@index.route('/salut')
def salut(): #can not be the same name as the blueprint name
    return 'Bonjour tous le monde!'
