from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = FastAPI()

CITY = "Denver"
API_KEY = os.getenv("API_KEY", "74c7744a330c1b360b139fb015503bd8")

def get_weather():
    try:
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(weather_url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
    except Exception as e:
        return {
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@app.get("/infos")
def get_info():
    now = datetime.now()
    return {
        "current_time": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "weather": get_weather()
    }
