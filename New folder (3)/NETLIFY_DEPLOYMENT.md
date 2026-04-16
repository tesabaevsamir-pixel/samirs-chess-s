# Deploying Chess Game to Netlify

## Overview
- **Frontend:** HTML/CSS/JavaScript hosted on Netlify (FREE)
- **Backend:** Python Flask hosted on Render, Railway, or Replit (FREE)

## Step 1: Deploy Backend to Render (Recommended - Free)

1. Go to **render.com** and sign up (free)
2. Click **New +** → **Web Service**
3. Connect your GitHub repo (or upload files manually)
4. Settings:
   - **Name:** chess-game-api
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy**
6. Wait for deployment, copy your Render URL (e.g., `https://chess-game-api.onrender.com`)

**Make sure Render URL is permanent** before moving to next step.

## Step 2: Update Frontend API URL

In `templates/index.html`, change:
```javascript
const API_URL = 'http://localhost:5000/api';
```
To:
```javascript
const API_URL = 'https://chess-game-api.onrender.com/api';
```
(Replace with your actual Render URL)

## Step 3: Deploy Frontend to Netlify

### Option A: Using Netlify CLI (Recommended)

1. Install Netlify CLI:
   ```
   npm install -g netlify-cli
   ```

2. From your project folder, run:
   ```
   cd c:\Users\admir\Desktop\New folder (3)
   netlify deploy --prod --dir=.
   ```

3. Login when prompted (creates account if needed)
4. Choose to deploy as new site
5. Your site will be live at a netlify URL (e.g., `https://your-site.netlify.app`)

### Option B: Drag & Drop (Easiest)

1. Go to **netlify.com** and sign up
2. Drag & drop your project folder into Netlify
3. Wait for deployment
4. Get your public URL

### Option C: GitHub Integration

1. Push your files to GitHub
2. Go to netlify.com → **New site from Git**
3. Connect GitHub, select repo
4. Deploy settings:
   - Build command: (leave empty)
   - Publish directory: (leave empty or `.`)
5. Click Deploy

## Step 4: Test Your Live Game

1. Visit your Netlify URL
2. The frontend should load
3. Moves should work with your Render backend

## Troubleshooting

### CORS Error in Console
Your Flask backend might need CORS enabled. Check `app.py` has:
```python
from flask_cors import CORS
CORS(app)
```

### Backend returns 404
- Check that Render deployment succeeded
- Verify API_URL in `index.html` matches your Render URL exactly
- Test the backend URL directly in browser (add `/api/board`)

### Site shows but doesn't load board
- Open browser DevTools (F12)
- Check Console tab for errors
- Verify backend is still running on Render

## Important Notes

- **Netlify** hosts static files only (UI)
- **Render** hosts Python backend (logic)
- Free tiers may sleep if unused for 15 mins (first request will be slow)
- Consider upgrading to paid tiers for production use

## Alternative Backend Hosting

If Render doesn't work, try:
- **Railway.app** - Similar to Render, free tier
- **Replit** - Easiest but may be slower
- **Heroku** - Phasing out free tier
- **PythonAnywhere** - Free with limitations

## Custom Domain (Optional)

1. Buy domain from GoDaddy, Namecheap, etc.
2. Go to **Netlify Settings → Domain Management**
3. Add your custom domain
4. Follow DNS setup instructions
5. Point DNS records to Netlify nameservers

Your chess game will now be live on the internet! 🎉
