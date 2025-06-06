from flask import Blueprint, request, jsonify
from models import db, User

api_bp = Blueprint('api', __name__)

# POST /users – Benutzer anlegen
@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    setup_name = data.get('setup_name')
    cpe = data.get('cpe')
    wlan = data.get('wlan')
    setup_type = data.get('setup_type')

    if not name or not email:
        return jsonify({"error": "Name und E-Mail sind erforderlich"}), 400

    user = User(
        name=name,
        email=email,
        setup_name=setup_name,
        cpe=cpe,
        wlan=wlan,
        setup_type=setup_type
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User erstellt",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "setup_name": user.setup_name,
            "cpe": user.cpe,
            "wlan": user.wlan,
            "setup_type": user.setup_type
        }
    }), 201

# GET /users – Alle Benutzer abrufen
@api_bp.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "setup_name": u.setup_name,
            "cpe": u.cpe,
            "wlan": u.wlan,
            "setup_type": u.setup_type
        }
        for u in users
    ])

# GET /users/<id> – Einzelnen Benutzer abrufen
@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User nicht gefunden"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "setup_name": user.setup_name,
        "cpe": user.cpe,
        "wlan": user.wlan,
        "setup_type": user.setup_type
    })

# PUT /users/<id> – Benutzer aktualisieren
@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User nicht gefunden"}), 404

    data = request.get_json()

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.setup_name = data.get('setup_name', user.setup_name)
    user.cpe = data.get('cpe', user.cpe)
    user.wlan = data.get('wlan', user.wlan)
    user.setup_type = data.get('setup_type', user.setup_type)

    db.session.commit()

    return jsonify({
        "message": "User aktualisiert",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "setup_name": user.setup_name,
            "cpe": user.cpe,
            "wlan": user.wlan,
            "setup_type": user.setup_type
        }
    })

# DELETE /users/<id> – Benutzer löschen
@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User nicht gefunden"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": f"User mit ID {user_id} wurde gelöscht."})
