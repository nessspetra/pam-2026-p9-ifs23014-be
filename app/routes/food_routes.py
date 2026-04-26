from flask import Blueprint, request, jsonify
from app.services.food_service import (
    create_foods,
    get_all_foods
)
from flask_jwt_extended import jwt_required

food_bp = Blueprint("food", __name__)

@food_bp.route("/", methods=["GET"])
def index():
    return "API telah berjalan! Dibuat Gayus Kelas Berkelas"
    

@food_bp.route("/foods/generate", methods=["POST"])
@jwt_required()

def generate():
    data = request.get_json()
    theme = data.get("theme")
    total = data.get("total")

    if not theme:
        return jsonify({"error": "Theme is required"}), 400
    
    if not total:
        return jsonify({"error": "Total is required"}), 400
    
    if total <= 0:
        return jsonify({"error": "Total harus besar dari 0"}), 400
    
    if total > 10:
        return jsonify({"error": "Total maksimal harus 10"}), 400

    try:
        result = create_foods(theme, total)

        return jsonify({
            "theme": theme,
            "total": len(result),
            "data": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@food_bp.route("/foods", methods=["GET"])
def get_all():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=100, type=int)

    data = get_all_foods(page=page, per_page=per_page)

    return jsonify(data)