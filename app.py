from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from api import api_bp

app = Flask(__name__)

# Render PostgreSQL-Verbindung
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://meineapiuser:gk2u1YcUpTDkqVlhZY0U0qAtGcBWxXcD@dpg-cvrvbcur433s73eaj0k0-a.oregon-postgres.render.com/meineapidb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
