# Weather App - FastAPI + HTML/CSS/JavaScript

A beautiful, fully functional weather application built with FastAPI backend and vanilla JavaScript frontend.

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r Requirements.txt
   ```

2. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Add your OpenWeatherMap API key:
     ```
     API_KEY=your_actual_openweather_api_key
     ```

## Running the App

### Option 1: Using the batch file (Windows)
```bash
run.bat
```

### Option 2: Using PowerShell/Terminal
```bash
uvicorn weather:app --reload --host 0.0.0.0 --port 8000
```

Then open your browser and go to: **http://localhost:8000**

## Features

- ✅ Real-time weather lookup by city name
- ✅ Beautiful, Apple-inspired UI with glassmorphism
- ✅ Shows temperature, feels like, humidity, and wind speed
- ✅ Error handling with user-friendly messages
- ✅ Fully responsive design
- ✅ Server-side API key management (secure)

## Project Structure

```
Weather app/
├── weather.py           # FastAPI backend
├── index.html           # Frontend HTML
├── styles.css           # Frontend styles
├── script.js            # Frontend JavaScript
├── Requirements.txt     # Python dependencies
├── .env                 # Environment variables (API_KEY)
├── .env.example         # Template for .env
├── Procfile             # Deployment config
└── run.bat              # Windows startup script
```

## API Endpoint

The backend provides a single endpoint:

- **GET** `/weather?city=london`
  - Returns JSON with weather data from OpenWeatherMap
  - Handled server-side with secure API key

## Deployment

For deployment to platforms like Heroku, Render, or similar:
1. Ensure `Requirements.txt` is present
2. Use the provided `Procfile`
3. Set environment variable `API_KEY` in your hosting platform
4. Deploy!

## Technologies Used

- **Backend**: FastAPI + Uvicorn
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: OpenWeatherMap REST API
- **Environment**: python-dotenv
