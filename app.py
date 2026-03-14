from flask import Flask, render_template, Response
from pathlib import Path

app = Flask(__name__)

# ログファイルの場所
ACCESS_LOG = Path("/var/log/nginx/access.log")
ERROR_LOG = Path("/var/log/nginx/error.log")

def tail_text(path: Path, n_lines: int = 200) -> str:
    if not path.exists():
        return f"{path} not found"
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    return "\n".join(lines[-n_lines:]) + "\n"

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/logs/access")
def show_access():
    content = tail_text(ACCESS_LOG, 200)
    return Response(content, mimetype="text/plain")

@app.get("/logs/error")
def show_error():
    content = tail_text(ERROR_LOG, 200)
    return Response(content, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
