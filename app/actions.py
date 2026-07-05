import os
import subprocess
from pathlib import Path
from .utils import timestamp_filename, is_safe_url, write_text_file


def action_notepad():
    try:
        subprocess.Popen(["notepad.exe"])
        return {"ok": True, "action": "notepad"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def action_calc():
    try:
        subprocess.Popen(["calc.exe"])
        return {"ok": True, "action": "calc"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def action_open_url(url):
    if not is_safe_url(url):
        return {"ok": False, "error": "unsafe or missing URL"}
    try:
        # Use cmd start to open default browser on Windows
        subprocess.Popen(["cmd", "/c", "start", "", url], shell=False)
        return {"ok": True, "action": "open-url", "url": url}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def action_note(text):
    home = Path.home()
    desktop = home / "Desktop"
    desktop.mkdir(parents=True, exist_ok=True)
    filename = timestamp_filename("note", ".txt")
    path = desktop / filename
    try:
        write_text_file(path, text)
        return {"ok": True, "path": str(path)}
    except Exception as e:
        return {"ok": False, "error": str(e)}
