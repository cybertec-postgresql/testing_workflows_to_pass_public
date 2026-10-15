from flask import Flask, make_response

app = Flask(__name__)

@app.route("/login")
def login():
    resp = make_response("Logged in")
    
    # 1. CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute
    # Semgrep Level: WARNING | CVSS: ~4.3 - 5.3 (Medium)
    # Cookie wird ohne 'secure=True' und 'httponly=True' gesetzt
    resp.set_cookie("session_id", "xyz123", secure=False, httponly=False)
    return resp
