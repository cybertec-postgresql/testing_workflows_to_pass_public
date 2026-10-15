import requests

def fetch_insecure(url: str):
    # Triggers CWE-295 (Disabled Certificate Validation -> CVSS ~5.3 - 7.5)
    return requests.get(url, verify=False)
