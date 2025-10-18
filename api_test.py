import google.generativeai as genai
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# API Key'i yapılandır
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini 2.0 Flash - Hızlı + Ücretsiz + Yüksek limit
model = genai.GenerativeModel('models/gemini-2.0-flash')  # ⬅️ 2.0 Flash!

try:
    # Test sorusu gönder
    response = model.generate_content("Merhaba! Sen kimsin? Türkçe olarak kısaca tanıt kendini.")

    print("=" * 60)
    print("✅ API TESTİ BAŞARILI!")
    print("=" * 60)
    print(f"\n🤖 Model: gemini-2.0-flash")
    print(f"⚡ Hız: Çok Hızlı | 💰 Ücretsiz Limit: Yüksek")
    print(f"\n💬 Cevap:\n{response.text}")
    print("\n" + "=" * 60)
    print("\n🎉 Artık RAG projesine başlayabiliriz!")

except Exception as e:
    print("=" * 60)
    print("❌ HATA OLUŞTU!")
    print("=" * 60)
    print(f"\nHata Detayı: {e}")