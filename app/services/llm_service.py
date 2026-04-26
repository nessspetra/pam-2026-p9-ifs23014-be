import google.generativeai as genai
from app.config import Config

# Konfigurasi API Key Gemini
genai.configure(api_key=Config.GEMINI_API_KEY)

def generate_from_llm(prompt: str):
    try:
        # Menggunakan model Gemini 1.5 Flash (cepat dan efisien)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Mengirim prompt ke Gemini
        response = model.generate_content(prompt)
        
        if not response.text:
            raise Exception("Gemini tidak mengembalikan teks")

        # Kita kembalikan dalam format dictionary agar sesuai 
        # dengan ekspektasi parser.py Anda sebelumnya
        return {"response": response.text}

    except Exception as e:
        raise Exception(f"Gagal menghubungi Gemini API: {str(e)}")