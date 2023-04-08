import os

class config():

    #generic config 
    SECRET_KEY = 'your-secret-key-here' #increase security, necessary for wtf
    BOOTSTRAP_SERVE_LOCAL = True #is a configuration option for Flask-Bootstrap that determines whether to serve the CSS and JavaScript files from a local copy or from a CDN (Content Delivery Network).
    
    #for google authentication purposes
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)

    @staticmethod
    def init_app(app):
        pass