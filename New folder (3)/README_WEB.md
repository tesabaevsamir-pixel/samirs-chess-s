# Chess Game - Web Version

A web-based chess game with AI opponent built with Flask (Python backend) and HTML/CSS/JavaScript.

## Files

- `app.py` - Flask backend server handling chess logic
- `templates/index.html` - Frontend UI
- `requirements.txt` - Python dependencies

## Installation

1. Ensure Python 3.6+ is installed
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Locally

1. Start the Flask backend:
   ```
   python app.py
   ```
   The server will run on `http://localhost:5000`

2. Open your browser to `http://localhost:5000`

3. Play the game! Click pieces to select, then click destination squares to move.
   - Green dots = possible moves
   - Red dots = captures
   - You play as White, AI plays as Black

4. Click "New Game" to reset

## Deploying to the Internet

To host this online, you need:

1. **Web Hosting with Python Support:**
   - Heroku (free tier limited)
   - PythonAnywhere
   - Replit
   - AWS/DigitalOcean (paid)

2. **For Heroku:**
   - Create a `Procfile`:
     ```
     web: gunicorn app:app
     ```
   - Add to requirements.txt:
     ```
     gunicorn
     ```
   - Push to Heroku

3. **For PythonAnywhere:**
   - Upload files via web interface
   - Configure Flask app in web settings
   - Set up domain

4. **For Static Hosting (Netlify/Vercel):**
   - You'd need to refactor to use an external API endpoint
   - Keep `index.html` as standalone frontend
   - Host API separately on a Python service

## Features

- Full chess rules enforcement
- AI opponent with random moves
- Move validation with visual feedback
- Beautiful responsive design
- Real-time game state

## How It Works

- **Backend (app.py):** Manages chess engine, validates moves, makes AI decisions
- **Frontend (index.html):** Displays board, handles user clicks, communicates with backend via REST API
- **Communication:** HTTP requests send moves, responses contain updated board state

## Troubleshooting

- Port 5000 already in use? Change `port=5000` in `app.py` to another port
- CORS errors? Flask-CORS is configured to allow cross-origin requests
- Pieces not showing? Ensure you're using a modern browser with Unicode support

## To Improve

- Upgrade AI to use Stockfish or minimax algorithm
- Add move history/undo
- Add player ratings/stats
- Add sound effects
- Add piece images instead of symbols
