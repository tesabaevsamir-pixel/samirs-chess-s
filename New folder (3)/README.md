# Simple Chess Game

A basic GUI-based chess game implemented in Python using the `chess` library and Tkinter.

## Usage

1. Ensure Python 3.6+ is installed (Tkinter is built-in).
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python main.py`
4. The game opens in full-screen mode. Press Escape to exit full-screen if needed.
5. You play as White; the AI plays as Black with random moves.
6. Click on a piece to select it (highlighted in red), then click on a destination square to move.
7. Possible moves are shown with green dots; captures with red dots.
8. The game alternates turns automatically after your move.
9. Game ends when checkmate, stalemate, or other termination conditions are met, showing a popup.

## Features

- Full-screen display with dynamic board sizing
- AI opponent (random moves for Black)
- Move highlighting: red outline for selected piece, green dots for possible moves, red dots for captures
- Full chess rules enforcement
- Move validation
- Graphical board with Unicode piece symbols
- Turn-based play with status display
- Game over notification

## Troubleshooting

- If you get import errors, ensure the `chess` library is installed: `pip install chess`
- Tkinter should be available by default; if not, install it via your OS package manager (e.g., `sudo apt install python3-tk` on Ubuntu).
- Moves must be valid; invalid selections are ignored.
- For advanced features (like better AI, sound effects), consider extending the code or using additional libraries.