from flask import Flask
from flask_login import LoginManager

from blueprints.auth.models import Users
from blueprints.main.views import main
from blueprints.auth.views import auth

from db.db import db


def create_app():
    data_wrangling = Flask(__name__)
    
    # setup with development configuration
    data_wrangling.config.from_object('config.DevelopmentConfig')
    
    # setup all our dependencies
    db.init_app(data_wrangling)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(data_wrangling)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    # register blueprints
    data_wrangling.register_blueprint(main)
    data_wrangling.register_blueprint(auth, url_prefix="/auth")

    return data_wrangling

if __name__ == "__main__":
    create_app().run()