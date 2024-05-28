from mixologymaster import db
from flask_login import UserMixin

class User (db.Model, UserMixin):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return str(self.id)
    
