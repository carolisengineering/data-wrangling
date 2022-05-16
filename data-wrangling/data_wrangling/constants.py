import os

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = 'data_wrangling'
FLASK_SECRET_KEY = 'flask_secret_key'
PRODUCTION_DATABASE_URL = os.environ.get('PRODUCTION_DATABASE_URL')
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)