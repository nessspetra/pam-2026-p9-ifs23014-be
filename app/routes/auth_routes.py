from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from app.config import Config

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Cek kredensial berdasarkan data di .env (Admin Statis)
    if username != Config.ADMIN_USERNAME or password != Config.ADMIN_PASSWORD:
        return jsonify({"error": "Username atau password salah"}), 401

    # Buat token JWT
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    # Untuk logout di JWT tanpa database blacklist, 
    # biasanya client cukup menghapus token di sisi mereka.
    return jsonify({"message": "Berhasil logout secara lokal"}), 200