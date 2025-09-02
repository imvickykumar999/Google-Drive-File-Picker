from flask import Flask, request, jsonify, send_from_directory, abort, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# Where to save files (ensure it exists)
UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Optional: limit request size (e.g. 50MB)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

# CORS for your front-end origin(s)
CORS(app, resources={r"/upload": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500"]}})

@app.post("/upload")
def upload():
    f = request.files.get("file")
    if not f:
        return ("No file field named 'file'", 400)

    # Make filename safe and unique
    original = secure_filename(f.filename or "unnamed")
    stamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S-%f")
    name_parts = original.rsplit(".", 1)
    if len(name_parts) == 2:
        base, ext = name_parts
        filename = f"{base}-{stamp}.{ext}"
    else:
        filename = f"{original}-{stamp}"

    save_path = UPLOAD_DIR / filename
    f.save(save_path)                              # <-- actually writes the file

    return jsonify({
        "saved_as": filename,
        "abs_path": str(save_path.resolve()),
        "rel_dir": str(UPLOAD_DIR.resolve()),
        "size": save_path.stat().st_size,
        "download_url": f"/uploads/{filename}",
    })

# Static-like route to serve uploaded files back (for testing)
@app.get("/uploads/<path:filename>")
def get_upload(filename):
    try:
        return send_from_directory(UPLOAD_DIR, filename, as_attachment=False)
    except FileNotFoundError:
        abort(404)

@app.get("/")
def home():
    return render_template(
        "index.html",
        CLIENT_ID=os.getenv("GOOGLE_CLIENT_ID", ""),
        API_KEY=os.getenv("GOOGLE_API_KEY", "")
    )

if __name__ == "__main__":
    app.run(port=5500, debug=True)
