# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# #from .models import User

# __version__ = '0.1.1'
# basedir = os.path.abspath(os.path.dirname(__file__))
# db=SQLAlchemy()

# def create_app():
#     app = Flask(__name__)

#     app.config['SECRET_KEY'] = 'secret-key-goes-here'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

#     db.init_app(app)

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app

# #db = SQLAlchemy(app=create_app())