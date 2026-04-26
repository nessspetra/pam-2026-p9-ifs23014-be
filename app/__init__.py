from flask import Flask
from flask_cors import CORS
from app.extensions import Base, engine, jwt # Tambahkan jwt
from app.routes.food_routes import food_bp
from app.routes.auth_routes import auth_bp # Tambahkan ini

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config') # Load semua config
    
    CORS(app)
    jwt.init_app(app) # Inisialisasi JWT

    Base.metadata.create_all(bind=engine)

    app.register_blueprint(food_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth") # Register auth

    return app