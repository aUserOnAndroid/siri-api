@echo off
REM Windows batch helper to run Flask
set FLASK_APP=app.main
if "%FLASK_ENV%"=="" set FLASK_ENV=development
python -m flask run --host=0.0.0.0 --port=5000
pause
