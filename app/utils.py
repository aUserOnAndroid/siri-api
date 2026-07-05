import os
import json
from datetime import datetime
from urllib.parse import urlparse


def timestamp_filename(prefix="note", ext=".txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{prefix}_{timestamp}{ext}"


def is_safe_url(url):
    # Very simple URL check - ensure scheme is http or https and has a netloc
    try:
        p = urlparse(url)
        return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False


def write_text_file(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path
