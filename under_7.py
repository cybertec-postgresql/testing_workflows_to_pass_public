import tempfile
from flask import Flask, make_response

app = Flask(__name__)

@app.route("/low-and-medium")
def low_and_medium():
    # 1. LOW (CVSS: 3.1 | CWE-614) -> Gate Status: Low
    # Cookie without 'secure' and 'httponly' flags
    resp = make_response("Testing < 7.0 threshold")
    resp.set_cookie("session_id", "xyz123", secure=False, httponly=False)

    # 2. MEDIUM (CVSS: ~4.0 - 5.5 | CWE-377) -> Gate Status: Medium
    # Insecure temporary file creation (predictable filename)
    tmp_file = tempfile.mktemp(suffix=".tmp")
    with open(tmp_file, "w") as f:
        f.write("temp data")

    return resp
