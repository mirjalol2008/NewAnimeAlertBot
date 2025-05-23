import requests
from config import ANIME_API_URL

def get_latest_anime():
    url = f"{ANIME_API_URL}/seasons/now"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print("API dan anime olishda xatolik:", e)
        return []