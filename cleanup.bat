@echo off
echo Cleaning up unnecessary files...
echo.

REM Delete documentation files
del /Q MYSQL_SETUP.md 2>nul
del /Q MONGODB_SETUP.md 2>nul
del /Q MONGODB_QUICK.txt 2>nul
del /Q MONGODB_SIMPLE.md 2>nul
del /Q DATABASE_SETUP.md 2>nul
del /Q DATABASE_COMPLETE.md 2>nul
del /Q QUICK_DB_SETUP.txt 2>nul
del /Q DASHBOARD_FIX.md 2>nul
del /Q TROUBLESHOOTING.md 2>nul
del /Q QUICKSTART.md 2>nul
del /Q README_ADVANCED.md 2>nul
del /Q FIXES_APPLIED.md 2>nul
del /Q note_updated.txt 2>nul
del /Q fix_csv.py 2>nul

REM Delete backup CSV
del /Q submissions_backup.csv 2>nul

REM Delete pycache
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

REM Delete .pyc files
del /s /q *.pyc 2>nul

echo.
echo Cleanup complete!
echo.
echo Deleted files:
echo - Extra documentation files
echo - Backup CSV files
echo - Python cache files
echo - .pyc files
echo.
pause
