from flask import Blueprint, request, jsonify
from models import db, User

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name und E-Mail sind erforderlich"}), 400

    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User erstellt", "user": {"id": user.id, "name": user.name, "email": user.email}}), 201

@api_bp.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ])
