from flask import Blueprint, redirect, url_for, current_app, request
from flask_login import current_user, login_user, logout_user
from authlib.integrations.flask_client import OAuth

from ..ext import oauth
from ..ext.db import db
from ..ext.loginManager import login_manager
from ..models import User

auth_goog = Blueprint('auth_goog', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@auth_goog.route('/test2')
def test2():
    google = current_app.config['google']
    print("this is google at route:{}".format(google))
    print("this is dir google at route:{}".format(dir(google)))
    print("this is google type at route:{}".format(type(google)))
    print("this is google tokens at route:{}".format(google.access_token_params))
    
    return "this is google at route:{}".format(google)

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
    user_name = user_info['name']
    user_email = user_info['email']
    user_profile_pic = user_info['picture']

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



    
    
    
'''    
    resp = google.authorized_response(grant_type='authorization_code')

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    else:
        access_token = resp['access_token']
        google_user = google.get('userinfo')
        user_id = google_user.data['id']
        user_name = google_user.data['name']
        user_email = google_user.data['email']
        user_profile_pic = google_user.data['picture']
        user = User.get(user_id)
        if not user:
            User.create(user_id, user_name, user_email, user_profile_pic)
        login_user(user)
        return redirect('/')
    
@auth_goog.route('/logout')
def logout():
    logout_user()
    return redirect('/')'''