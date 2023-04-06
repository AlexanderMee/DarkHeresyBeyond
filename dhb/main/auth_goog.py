from flask import Blueprint, redirect, url_for, current_app
from google.oauth2 import id_token
from google.auth.transport import requests


from ..ext import db
from ..ext import oauth
from ..ext.oauth import google
from ..ext.loginManager import login_manager, current_user
from ..models import User

auth_goog = Blueprint('auth_goog', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@auth_goog.route('/test2')
def test2():
    google = current_app.config['google']
    print("this is google at route:{}".format(google))
    return "this is google at route:{}".format(google)

@auth_goog.route('/goog')
def login():
    google = current_app.config['google']
    if current_user.is_authenticated:
        return redirect('http://127.0.0.1:5000/')
    else:
        return google.authorize(callback='http://127.0.0.1:5000/auth')

@auth_goog.route('/auth')
def auth():
    google = current_app.config['google']
    resp = google.authorized_response()
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
    return redirect('/')




'''
@auth_goog.route('/', methods=['POST'])
def login():
    token = request.json.get('id_token')
    try:
        # Verify and decode the Google Sign-In ID token
        info = id_token.verify_oauth2_token(token, requests.Request())
        user_id = info['sub']
        name = info['name']
        email = info['email']
        picture = info['picture']

        # Check if the user already exists in the database
        user = User.get(user_id)

        if not user:
            # Create a new user if they don't exist
            User.create(user_id, name, email, picture)

        # Log the user in using Flask-Login
        user = User.get(user_id)
        login_user(user)

        return redirect('/')
    
    except ValueError:
        # Invalid token
        return 'Invalid token', 400
 '''