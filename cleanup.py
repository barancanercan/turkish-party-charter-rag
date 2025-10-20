"""
Proje temizleme scripti
Gereksiz dosyaları experiments/ klasörüne taşır
"""

import os
import shutil
from pathlib import Path

# Root directory
ROOT = Path(__file__).parent

# Taşınacak dosyalar
files_to_move = [
    "api_test.py",
    "test.py",
]

# Experiments klasörü
experiments_dir = ROOT / "experiments" / "old_tests"
experiments_dir.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("🧹 PROJE TEMİZLİĞİ")
print("=" * 60)

# Dosyaları taşı
for filename in files_to_move:
    source = ROOT / filename
    if source.exists():
        dest = experiments_dir / filename
        shutil.move(str(source), str(dest))
        print(f"✅ Taşındı: {filename} -> experiments/old_tests/")
    else:
        print(f"⚠️ Bulunamadı: {filename}")

# ChromaDB temizle (eğer varsa)
chroma_db = ROOT / "chroma_db"
if chroma_db.exists() and list(chroma_db.iterdir()):
    print(f"\n⚠️ chroma_db/ klasörü içinde dosyalar var.")
    print(f"   Bu klasör .gitignore'da, silinebilir.")
else:
    print(f"\n✅ chroma_db/ klasörü temiz.")

print("\n" + "=" * 60)
print("✅ Temizlik tamamlandı!")
print("=" * 60)

print("\n📁 Yeni Proje Yapısı:")
print("""
turkish-party-charter-rag/
├── data/party_charters/     ✅ Parti tüzükleri
├── src/                     ✅ Ana kaynak kod
├── tests/                   ✅ Test dosyaları
├── notebooks/               ✅ Jupyter notebooks
├── experiments/             ✅ Deneysel çalışmalar
│   └── old_tests/          ✅ Eski test dosyaları
├── docs/                    ✅ Dokümantasyon
├── .env.example             ✅ Environment örneği
├── requirements.txt         ✅ Bağımlılıklar
└── README.md                ✅ Proje açıklaması
""")

print("\n📝 Sonraki Adımlar:")
print("1. python cleanup.py  (bu script'i çalıştır)")
print("2. git add .")
print("3. git commit -m 'chore: clean up project structure'")
print("4. git push origin main")
