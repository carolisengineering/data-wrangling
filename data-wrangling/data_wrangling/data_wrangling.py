from flask import Flask

from blueprints.main.views import main
from blueprints.auth.views import auth

from db.db import db


def create_app():
    data_wrangling = Flask(__name__)
    
    # setup with development configuration
    data_wrangling.config.from_object('config.DevelopmentConfig')
    
    # setup all our dependencies
    db.init_app(data_wrangling)
    
    # register blueprints
    data_wrangling.register_blueprint(main)
    data_wrangling.register_blueprint(auth, url_prefix="/auth")

    return data_wrangling

if __name__ == "__main__":
    create_app().run()