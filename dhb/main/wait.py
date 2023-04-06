from flask import Blueprint

wait = Blueprint('wait', __name__)

@wait.route('/wait')
def hello(): #can not be the same name as the blueprint name
    return 'Hello World!'

