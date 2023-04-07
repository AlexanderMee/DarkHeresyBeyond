#from flask_oauthlib.client import OAuth
from authlib.integrations.flask_client import OAuth

oauth = OAuth()

google = None

def init_app(app):

    oauth.init_app(app)

    #global google

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

    '''  google = oauth.remote_app(
        'google',
        request_token_params={
            'scope': 'email profile openid'
        },
        base_url='https://www.googleapis.com/oauth2/v1/',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        request_token_url=None,
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_method='POST',
        #access_token_params={'grant_type': 'authorization_code'},
        access_token_params=None,
        consumer_key=app.config['GOOGLE_CLIENT_ID'],
        consumer_secret=app.config['GOOGLE_CLIENT_SECRET']
    ) 
    '''
    #this has to go within the function bevause it relies on config which occurs before extentions
    print("this is google at ext:{}".format(google))

    return google