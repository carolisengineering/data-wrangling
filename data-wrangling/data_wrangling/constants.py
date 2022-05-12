import os

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = 'data_wrangling'
PRODUCTION_DATABASE_URL = os.environ.get('PRODUCTION_DATABASE_URL')