# PowerShell helper to run the Flask app
# Usage: .\run.ps1
$env:FLASK_APP = "app.main"
$env:FLASK_ENV = (Get-Item -Path env:FLASK_ENV -ErrorAction SilentlyContinue).Value
if (-not $env:FLASK_ENV) { $env:FLASK_ENV = "development" }
python -m flask run --host=0.0.0.0 --port=5000
