# Quick Start: Deploy to Netlify

## 1️⃣ Deploy Backend (Choose One)

### Easiest: Render.com
1. Go to **render.com** → Sign up
2. Click **New Web Service**
3. Upload/connect this folder
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Click Deploy, wait ~2 mins
7. Copy your URL (e.g., `https://chess-game-api.onrender.com`)

## 2️⃣ Update Frontend API URL

In `index.html`, find this line (around line 165):
```javascript
API_URL = 'https://chess-game-api.onrender.com/api';
```
Replace with your actual Render URL.

## 3️⃣ Deploy Frontend to Netlify

### Option A (Easiest): Drag & Drop
1. Go to **netlify.com** → Sign up
2. Drag your project folder onto the browser
3. Done! Your site is live.

### Option B: CLI
```
npm install -g netlify-cli
netlify deploy --prod
```

### Option C: GitHub
1. Push folder to GitHub
2. Netlify → New site from Git
3. Select repo → Deploy

## ✅ Test It
- Visit your Netlify URL
- Click pieces to play
- Should work with AI

## 📝 Important
- **Netlify** = Frontend (green checkmark)
- **Render** = Backend (green checkmark)
- Both must be deployed for game to work
- Make sure API URL in `index.html` matches your backend

## Need Help?
See `NETLIFY_DEPLOYMENT.md` for detailed troubleshooting
