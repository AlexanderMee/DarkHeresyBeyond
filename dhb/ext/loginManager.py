from flask_login import LoginManager, current_user

login_manager = LoginManager()
current_user = current_user

#for login manager I've used camelCase for the module name, under_score for the custom instance, this is so I can see what works where

def init_app(app):
    login_manager.init_app(app)

    # Custom initialization code here, if needed