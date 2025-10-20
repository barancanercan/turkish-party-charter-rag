@echo off
REM Git komutları - Windows Batch File

echo ==================================
echo GIT CLEANUP ^& PUSH
echo ==================================

REM 1. Git durumunu kontrol et
echo.
echo 1. Git Status...
git status

REM 2. Tüm değişiklikleri stage'e al
echo.
echo 2. Staging all changes...
git add .

REM 3. Git status tekrar (staged dosyalar)
echo.
echo 3. Staged files:
git status

REM 4. Commit
echo.
echo 4. Committing...
git commit -m "chore: clean up project structure and update README" -m "- Moved old test files to experiments/old_tests/" -m "- Updated README with comprehensive documentation" -m "- Added cleanup script for maintenance" -m "- Organized project structure"

REM 5. Push
echo.
echo 5. Pushing to origin main...
git push origin main

echo.
echo ==================================
echo TAMAMLANDI!
echo ==================================

pause
