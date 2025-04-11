from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    setup_name = db.Column(db.String(100), nullable=True)
    cpe = db.Column(db.String(100), nullable=True)
    wlan = db.Column(db.String(100), nullable=True)
    setup_type = db.Column(db.String(100), nullable=True)
