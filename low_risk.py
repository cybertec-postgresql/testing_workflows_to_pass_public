import hashlib

def get_hash(text: str) -> str:
    # CWE-328: Weak Hash (CVSS unter 8.0)
    return hashlib.md5(text.encode("utf-8")).hexdigest()
