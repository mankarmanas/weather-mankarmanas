@echo off
echo Starting Weather App...
echo.
echo Make sure .env file has your OpenWeatherMap API_KEY
echo.
uvicorn weather:app --reload --host 0.0.0.0 --port 8000
pause
