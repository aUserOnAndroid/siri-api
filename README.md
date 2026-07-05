# siri-api

A beginner-friendly Python Flask web API you can run on Windows and trigger from iOS Shortcuts (Siri).

This repo provides small, safe endpoints you can call from Shortcuts; add a voice phrase in Shortcuts to trigger them via Siri.

Quickstart (Windows)
1. Install Python 3.8+ from https://python.org
2. Clone the repo and change directory:
   git clone https://github.com/aUserOnAndroid/siri-api.git
   cd siri-api
3. Create a virtual environment and install dependencies:
   python -m venv .venv
   .\\.venv\\Scripts\\activate
   pip install -r requirements.txt
4. Copy .env.example to .env and set an API_KEY value:
   copy .env.example .env
   (open .env in Notepad and replace API_KEY=change_me with a secure key)
5. Run the server:
   PowerShell: .\\run.ps1
   or: .\\run.bat
6. (Optional) Expose to the internet for Shortcuts/Siri testing:
   ngrok http 5000
   Use the https URL ngrok gives in your Shortcut.

Security
- The server requires an API key (header X-API-Key or query param api_key). Keep it secret.
- The /run endpoint ONLY accepts a small whitelist of safe actions (open Notepad, Calculator, open a URL). It will NOT run arbitrary shell commands.
- When testing remotely, prefer ngrok and a short-lived API key.

Contents
- app/ - the Flask app
- examples/shortcuts/ - instructions for creating Shortcuts that call this API
- run.ps1 / run.bat - helper scripts to run the server on Windows
- .env.example - environment variables (API key)

See examples/shortcuts/README.md for step-by-step Shortcut instructions and how to map a voice phrase to a Shortcut in iOS.
