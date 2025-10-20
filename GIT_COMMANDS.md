# 🚀 GIT KOMUTLARI - MANUAL

## Terminal'de şu komutları sırayla çalıştır:

```bash
# 1. Proje dizinine git
cd C:\Users\user\Desktop\LLMProject\turkish-party-charter-rag

# 2. Git durumunu kontrol et
git status

# 3. Tüm değişiklikleri stage'e al
git add .

# 4. Hangi dosyaların staged olduğunu gör
git status

# 5. Commit yap
git commit -m "chore: clean up project structure and update README" -m "- Moved old test files to experiments/old_tests/" -m "- Updated README with comprehensive documentation" -m "- Added cleanup and git scripts" -m "- Organized project structure for better maintainability"

# 6. Remote'a push et
git push origin main

# 7. Kontrol et
git log --oneline -n 5
```

## ✅ Beklenen Değişiklikler:

**Yeni Dosyalar:**
- experiments/old_tests/api_test.py
- experiments/old_tests/test.py
- cleanup.py
- git_push.bat
- git_push.sh
- GIT_COMMANDS.md

**Güncellenen Dosyalar:**
- README.md (tamamen yenilendi)

**Silinen Dosyalar:**
- api_test.py (taşındı)
- test.py (taşındı)

## 🔍 Push Sonrası Kontrol:

GitHub'da kontrol et:
https://github.com/barancanercan/turkish-party-charter-rag

**Kontrol edilecekler:**
- ✅ README.md güncel mi?
- ✅ Eski test dosyaları experiments/old_tests/ içinde mi?
- ✅ Root dizin temiz mi?
- ✅ Commit message anlamlı mı?

## 📝 Alternatif: Otomatik Script

```bash
# Windows CMD/PowerShell:
git_push.bat

# Git Bash / Linux / Mac:
bash git_push.sh
```

---

**Hazır mısın?** Terminal'i aç ve komutları çalıştır! 🚀
