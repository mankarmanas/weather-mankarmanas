# Deployment Guide

## GitHub Setup

### 1. Create a GitHub Repository
- Go to [github.com/new](https://github.com/new)
- Name it: `weather-app`
- Add description: "Real-time Weather App with FastAPI and OpenWeatherMap API"
- **Do NOT initialize** with README (we'll push from command line)

### 2. Initialize Git Locally
Open PowerShell in your project folder and run:

```bash
git init
git add .
git commit -m "Initial commit: Weather app with FastAPI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/weather-app.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Vercel Deployment

### Prerequisites
- GitHub repository created (from above steps)
- Vercel account at [vercel.com](https://vercel.com) (sign in with GitHub)

### 1. Connect to Vercel
1. Go to [vercel.com/new](https://vercel.com/new)
2. Click "Import Project"
3. Select "Import Git Repository"
4. Paste: `https://github.com/YOUR_USERNAME/weather-app.git`
5. Click "Import"

### 2. Configure Environment Variables
1. In Vercel dashboard, go to **Settings > Environment Variables**
2. Add:
   - **Name:** `API_KEY`
   - **Value:** `your_openweathermap_api_key`
3. Click "Add"

### 3. Deploy
1. Click the "Deploy" button
2. Wait for deployment to complete (~3-5 minutes)
3. Your app will be live at: `https://your-project-name.vercel.app`

---

## Troubleshooting

- **"API_KEY is missing"**: Check Environment Variables in Vercel Settings
- **"Static files not found"**: This is normal for FastAPI + Vercel, your app should still work
- **Slow loads**: Cold starts are normal on Vercel's free tier

---

## After Deployment

- Test your live app: Visit your Vercel URL
- Share the link with anyone!
- Update code: Push changes to GitHub, Vercel auto-deploys
