import os

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = 'data_wrangling'
FLASK_SECRET_KEY = 'flask_secret_key'
PRODUCTION_DATABASE_URL = os.environ.get('PRODUCTION_DATABASE_URL')