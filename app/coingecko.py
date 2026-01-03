import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def get_project(coin_id: str):
    url = f"{BASE_URL}/coins/{coin_id}"
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return None
    return r.json()
