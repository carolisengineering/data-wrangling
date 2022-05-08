from db.db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, id_num: int, email: str, password: str,
                 name: str) -> None:
        self.id = id_num
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return f"User: {str(self.id)} - Name: {self.name}"