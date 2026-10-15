import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/run")
def run_cmd():
    # CWE-78: OS Command Injection (CVSS > 8.0)
    cmd = request.args.get("cmd")
    return subprocess.check_output(cmd, shell=True)

@app.route("/user")
def get_user():
    # CWE-89: SQL Injection (CVSS > 8.0)
    user = request.args.get("user")
    conn = sqlite3.connect("app.db")
    return str(conn.execute(f"SELECT * FROM users WHERE name = '{user}'").fetchall())
