import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests

load_dotenv()
api_key = os.getenv('API_KEY')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/weather')
async def weather_api(city: str):
    if not city or not city.strip():
        raise HTTPException(status_code=400, detail='Please enter a city name.')
    if not api_key:
        raise HTTPException(status_code=500, detail='Weather service temporarily unavailable. Please try again later.')

    try:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': api_key, 'units': 'metric'}
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            return JSONResponse(status_code=404, content={'error': f'City "{city}" not found. Please check the spelling.'})
        elif response.status_code != 200:
            return JSONResponse(status_code=response.status_code, content={'error': 'Unable to fetch weather data. Please try again.'})

        return response.json()
    except requests.exceptions.Timeout:
        return JSONResponse(status_code=500, content={'error': 'Request timed out. Please try again.'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': 'Unable to fetch weather data. Please try again later.'})

@app.get('/')
async def root():
    return FileResponse('../index.html')
