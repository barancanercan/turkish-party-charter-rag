import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# =============================================================================
# API KEYS (Güvenli - .env'den gelir)
# =============================================================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# =============================================================================
# MODEL CONFIGURATION
# =============================================================================
# Embedding Model (Turkish BERT - Test edildi ✅)
EMBEDDING_MODEL = "dbmdz/bert-base-turkish-cased"
EMBEDDING_DIMENSION = 768

# LLM Model (Gemini 2.0 Flash - Ücretsiz ✅)
LLM_MODEL = "models/gemini-2.0-flash"
LLM_TEMPERATURE = 0.7  # 0 = deterministik, 1 = yaratıcı
LLM_MAX_TOKENS = 1024

# =============================================================================
# RAG CONFIGURATION
# =============================================================================
# Document Chunking
CHUNK_SIZE = 1000  # Her chunk'ın boyutu (karakter)
CHUNK_OVERLAP = 200  # Chunk'lar arası overlap

# Retrieval
TOP_K_RESULTS = 3  # Kaç doküman döndürecek
SIMILARITY_THRESHOLD = 0.7  # Minimum benzerlik skoru

# =============================================================================
# VECTOR DATABASE (ChromaDB)
# =============================================================================
CHROMA_DB_DIR = "./chroma_db"
COLLECTION_NAME = "party_charters"

# =============================================================================
# DATA PATHS
# =============================================================================
DATA_DIR = "./data"
PARTY_CHARTERS_DIR = "./data/party_charters"

# =============================================================================
# APP CONFIGURATION (Streamlit)
# =============================================================================
APP_TITLE = "Turkish Party Charter Q&A"
APP_DESCRIPTION = """
Ask questions about Turkish political party charters and get accurate answers 
with source citations.
"""

# =============================================================================
# LOGGING
# =============================================================================
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR


# =============================================================================
# VALIDATION (Config yüklendiğinde kontrol et)
# =============================================================================
def validate_config():
    """Kritik ayarları kontrol et"""
    if not GEMINI_API_KEY:
        raise ValueError("❌ GEMINI_API_KEY not found in .env file!")

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"✅ Created {DATA_DIR}")

    if not os.path.exists(PARTY_CHARTERS_DIR):
        os.makedirs(PARTY_CHARTERS_DIR)
        print(f"✅ Created {PARTY_CHARTERS_DIR}")

    print("✅ Config validated successfully!")


# Config yüklendiğinde otomatik validate et
if __name__ != "__main__":
    validate_config()