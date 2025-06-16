from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
import requests
import uvicorn
load_dotenv()
app = FastAPI()
CITY = "Denver"
API_KEY = "74c7744a330c1b360b139fb015503bd8"
def get_weather():
    try:
       weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
       response = requests.get(weather_url)
       response.raise_for_status()  # Raise an error for bad responses
       data = response.json()
       weather = {
           "city": data["name"],
           "temperature": data["main"]["temp"],
           "description": data["weather"][0]["description"],
        #    "icon": data["weather"][0]["icon"],
        #    "humidity": data["main"]["humidity"],
        #    "wind_speed": data["wind"]["speed"],
        #    "timestamp": datetime.now().isoformat()
       }
    except requests.exceptions.RequestException as e:
         weather = {
              "error": str(e),
              "timestamp": datetime.now().isoformat()
         }
    return weather

@app.get("/info")
def get_info():
    current_time = datetime.now().isoformat()
    formated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formated_time = datetime.now().strftime("%H:%M:%S")
    weather = get_weather()
    return {
        "current_time": current_time,
        "date": formated_date,
        "time": formated_time,
        "weather": weather
    }