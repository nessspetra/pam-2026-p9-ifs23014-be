from app import create_app
from app.config import Config

app = create_app()

if __name__ == "__main__":
    # Menjalankan aplikasi sesuai port di .env atau default 5000
    app.run(host="0.0.0.0", port=8080, debug=False)