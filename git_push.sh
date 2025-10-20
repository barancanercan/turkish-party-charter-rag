#!/bin/bash
# Git komutları - Windows için PowerShell/CMD

echo "=================================="
echo "GIT CLEANUP & PUSH"
echo "=================================="

# 1. Git durumunu kontrol et
echo ""
echo "1️⃣ Git Status..."
git status

# 2. Tüm değişiklikleri stage'e al
echo ""
echo "2️⃣ Staging all changes..."
git add .

# 3. Git status tekrar (staged dosyalar)
echo ""
echo "3️⃣ Staged files:"
git status

# 4. Commit
echo ""
echo "4️⃣ Committing..."
git commit -m "chore: clean up project structure and update README

- Moved old test files to experiments/old_tests/
- Updated README with comprehensive project documentation
- Added cleanup script for project maintenance
- Organized project structure for better maintainability"

# 5. Push
echo ""
echo "5️⃣ Pushing to origin main..."
git push origin main

echo ""
echo "=================================="
echo "✅ TAMAMLANDI!"
echo "=================================="
