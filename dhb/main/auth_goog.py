from flask import Blueprint, redirect, url_for, current_app
from flask_login import current_user, login_user, logout_user

from ..ext import oauth
from ..ext.db import db
from ..ext.loginManager import login_manager
from ..models import User

auth_goog = Blueprint('auth_goog', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth_goog.route('/goog')
def login():
    google = current_app.config['google']
    if current_user.is_authenticated:
        return redirect('http://127.0.0.1:5000/')
    else:
        redirect_uri = url_for('auth_goog.auth', _external=True)
        return google.authorize_redirect(redirect_uri)
    
@auth_goog.route('/auth')
def auth():
    google = current_app.config['google']
    token = google.authorize_access_token()
    resp = google.get('userinfo', token=token)
    user_info = resp.json()

    user_id = user_info['id']

    user = User.get(user_id)

    if not user:
        user = User.create(
            id_=user_info["id"],
            name=user_info["name"],
            email=user_info["email"],
            profile_pic=user_info["picture"],
        )

    login_user(user)
    return redirect('/')

@auth_goog.route('/logout')
def logout():
    logout_user()
    return redirect('/')
