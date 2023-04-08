from authlib.integrations.flask_client import OAuth

oauth = OAuth()

google = None #ok google needs to exist before it is imported by the factory, but its values are determined by config, whcih changes

def init_app(app):

    oauth.init_app(app)

    #create google object (must go after! i think)

    google = oauth.register(
        'google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        access_token_url='https://oauth2.googleapis.com/token',
        access_token_params={'grant_type': 'authorization_code'},
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        request_token_url=None,
        client_kwargs={'scope': 'email profile openid'}
    )

    #this has to go within the function bevause it relies on config which occurs before extentions

    return google