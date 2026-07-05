import os
import json
import subprocess
from datetime import datetime
from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "5000"))

app = Flask(__name__)

def check_api_key():
    key = request.headers.get("X-API-Key") or request.args.get("api_key")
    if not API_KEY or key != API_KEY:
        abort(401, description="Invalid or missing API key")

@app.route("/")
def index():
    return jsonify({"ok": True, "message": "siri-api ready"})

# /say - returns JSON containing the text to speak (Shortcuts will handle speaking)
@app.route("/say", methods=["GET"])
def say():
    check_api_key()
    text = request.args.get("text", "")
    if not text:
        return jsonify({"error": "missing 'text' parameter"}), 400
    return jsonify({"spoken": text})

# /note - create a timestamped text file on the Windows Desktop
@app.route("/note", methods=["POST"])
def note():
    check_api_key()
    data = request.get_json(silent=True) or request.form or {}
    text = data.get("text") or request.args.get("text")
    if not text:
        return jsonify({"error": "missing 'text' in JSON, form, or query"}), 400

    home = os.path.expanduser("~")
    desktop = os.path.join(home, "Desktop")
    os.makedirs(desktop, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"note_{timestamp}.txt"
    path = os.path.join(desktop, filename)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return jsonify({"ok": True, "path": path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# /run - run a safe, whitelisted action on Windows
@app.route("/run", methods=["POST", "GET"])
def run_action():
    check_api_key()
    # Accept either JSON or query params
    data = request.get_json(silent=True) or request.form or {}
    action = data.get("action") or request.args.get("action")
    if not action:
        return jsonify({"error": "missing 'action' parameter (e.g., notepad, calc, open-url)"}), 400

    # Whitelist actions
    if action == "notepad":
        try:
            subprocess.Popen(["notepad.exe"])
            return jsonify({"ok": True, "action": "notepad"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    if action == "calc":
        try:
            subprocess.Popen(["calc.exe"])
            return jsonify({"ok": True, "action": "calc"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    if action == "open-url":
        url = data.get("url") or request.args.get("url")
        if not url:
            return jsonify({"error": "missing 'url' parameter"}), 400
        try:
            # Use start to open URL with default browser
            subprocess.Popen(['cmd', '/c', 'start', '', url], shell=False)
            return jsonify({"ok": True, "action": "open-url", "url": url})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "action not allowed"}), 403

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
