from app import create_app
from app.config import Config
import os

app = create_app()

if __name__ == "__main__":
    # Menjalankan aplikasi sesuai port dari environment (untuk deployment) atau .env atau default 8080
    port = int(os.environ.get("PORT", Config.APP_PORT))
    app.run(host="0.0.0.0", port=port, debug=False)