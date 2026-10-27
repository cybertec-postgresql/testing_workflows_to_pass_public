import subprocess
import requests
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/test-all")
def test_all():
    # 1. LOW (CVSS: 3.1 | CWE-614) -> Gate Status: Low (blockiert NICHT)
    resp = make_response("Testing")
    resp.set_cookie("session_id", "xyz123", secure=False, httponly=False)

    # 2. HIGH (CVSS: 7.4 | CWE-295) -> Gate Status: High (BLOCKIERT jetzt, da >= 7.0!)
    requests.get("https://example.com", verify=False)

    # 3. CRITICAL (CVSS: 9.8 | CWE-78) -> Gate Status: Critical (BLOCKIERT, da >= 7.0!)
    cmd = request.args.get("cmd", "ls")
    subprocess.check_output(cmd, shell=True)

    return resp
