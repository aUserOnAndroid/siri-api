import os
from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "5000"))

from .actions import action_notepad, action_calc, action_open_url, action_note

app = Flask(__name__)
# Allow CORS for the simple web UI; requests still require API key
CORS(app)


def check_api_key():
    key = request.headers.get("X-API-Key") or request.args.get("api_key")
    if not API_KEY or key != API_KEY:
        abort(401, description="Invalid or missing API key")


@app.route("/")
def index():
    return jsonify({"ok": True, "message": "siri-api ready"})


@app.route("/say", methods=["GET"])
def say():
    check_api_key()
    text = request.args.get("text", "")
    if not text:
        return jsonify({"error": "missing 'text' parameter"}), 400
    return jsonify({"spoken": text})


@app.route("/note", methods=["POST"])
def note():
    check_api_key()
    data = request.get_json(silent=True) or request.form or {}
    text = data.get("text") or request.args.get("text")
    if not text:
        return jsonify({"error": "missing 'text' in JSON, form, or query"}), 400
    result = action_note(text)
    if result.get("ok"):
        return jsonify(result)
    return jsonify(result), 500


@app.route("/run", methods=["POST", "GET"])
def run_action():
    check_api_key()
    data = request.get_json(silent=True) or request.form or {}
    action = data.get("action") or request.args.get("action")
    if not action:
        return jsonify({"error": "missing 'action' parameter (e.g., notepad, calc, open-url)"}), 400

    if action == "notepad":
        return jsonify(action_notepad())

    if action == "calc":
        return jsonify(action_calc())

    if action == "open-url":
        url = data.get("url") or request.args.get("url")
        if not url:
            return jsonify({"error": "missing 'url' parameter"}), 400
        return jsonify(action_open_url(url))

    return jsonify({"error": "action not allowed"}), 403


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
