@echo off
echo ==========================================
echo    HERBARIUM PROJECT - GITHUB SETUP
echo ==========================================
ech.
echo 1. Initializing Git...
git init
if %errorlevel% neq 0 (
    echo [ERROR] Git init failed.
    pause
    exit /b
)

echo.
echo 2. Linking to Repository...
git remote remove origin 2>nul
git remote add origin https://github.com/herbariumoffical-lgtm/herbarium

echo.
echo 3. Staging Files...
git add .

echo.
echo 4. Committing...
git commit -m "Initial deploy by Antigravity"

echo.
echo ==========================================
echo    READY TO UPLOAD!
echo ==========================================
echo.
echo 5. Pushing to GitHub...
echo    (Please enter your Username and Password/Token if asked)
echo.
git push -u origin master --force

echo.
echo ==========================================
echo    DONE!
echo ==========================================
pause
