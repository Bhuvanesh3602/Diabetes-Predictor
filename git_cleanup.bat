@echo off
echo ========================================
echo GitHub Repository Cleanup Script
echo ========================================
echo.

REM Check if git is initialized
git status >nul 2>&1
if errorlevel 1 (
    echo Error: Not a git repository!
    echo Please run 'git init' first.
    pause
    exit /b 1
)

echo Step 1: Deleting unnecessary files...
echo.

REM Delete documentation files
if exist MYSQL_SETUP.md del MYSQL_SETUP.md && echo Deleted: MYSQL_SETUP.md
if exist MONGODB_SETUP.md del MONGODB_SETUP.md && echo Deleted: MONGODB_SETUP.md
if exist MONGODB_QUICK.txt del MONGODB_QUICK.txt && echo Deleted: MONGODB_QUICK.txt
if exist MONGODB_SIMPLE.md del MONGODB_SIMPLE.md && echo Deleted: MONGODB_SIMPLE.md
if exist DATABASE_SETUP.md del DATABASE_SETUP.md && echo Deleted: DATABASE_SETUP.md
if exist DATABASE_COMPLETE.md del DATABASE_COMPLETE.md && echo Deleted: DATABASE_COMPLETE.md
if exist QUICK_DB_SETUP.txt del QUICK_DB_SETUP.txt && echo Deleted: QUICK_DB_SETUP.txt
if exist DASHBOARD_FIX.md del DASHBOARD_FIX.md && echo Deleted: DASHBOARD_FIX.md
if exist TROUBLESHOOTING.md del TROUBLESHOOTING.md && echo Deleted: TROUBLESHOOTING.md
if exist QUICKSTART.md del QUICKSTART.md && echo Deleted: QUICKSTART.md
if exist README_ADVANCED.md del README_ADVANCED.md && echo Deleted: README_ADVANCED.md
if exist FIXES_APPLIED.md del FIXES_APPLIED.md && echo Deleted: FIXES_APPLIED.md
if exist note_updated.txt del note_updated.txt && echo Deleted: note_updated.txt
if exist fix_csv.py del fix_csv.py && echo Deleted: fix_csv.py
if exist CLEANUP_GUIDE.md del CLEANUP_GUIDE.md && echo Deleted: CLEANUP_GUIDE.md
if exist submissions_backup.csv del submissions_backup.csv && echo Deleted: submissions_backup.csv

echo.
echo Step 2: Staging changes...
git add -A

echo.
echo Step 3: Committing changes...
git commit -m "Clean up unnecessary documentation and backup files"

echo.
echo Step 4: Pushing to GitHub...
echo.
echo Choose your branch:
echo 1. main
echo 2. master
echo 3. Custom branch name
echo.
set /p branch_choice="Enter choice (1-3): "

if "%branch_choice%"=="1" (
    set branch=main
) else if "%branch_choice%"=="2" (
    set branch=master
) else if "%branch_choice%"=="3" (
    set /p branch="Enter branch name: "
) else (
    set branch=main
)

echo.
echo Pushing to branch: %branch%
git push origin %branch%

if errorlevel 1 (
    echo.
    echo Error: Push failed!
    echo Please check your internet connection and GitHub credentials.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Cleanup Complete!
echo ========================================
echo.
echo Files removed from GitHub:
echo - Extra documentation files
echo - Backup CSV files
echo - Temporary files
echo.
echo Your repository is now clean!
echo.
pause
