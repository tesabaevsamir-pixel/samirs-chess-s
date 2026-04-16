import chess
import random
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Global board state
game_state = {
    "board": chess.Board(),
    "ai_color": chess.BLACK
}

@app.route('/api/board', methods=['GET'])
def get_board():
    board = game_state["board"]
    return jsonify({
        "fen": board.fen(),
        "turn": "white" if board.turn == chess.WHITE else "black",
        "game_over": board.is_game_over(),
        "result": board.result() if board.is_game_over() else None,
        "legal_moves": [move.uci() for move in board.legal_moves]
    })

@app.route('/api/move', methods=['POST'])
def make_move():
    data = request.json
    move_uci = data.get("move")
    
    board = game_state["board"]
    
    try:
        move = chess.Move.from_uci(move_uci)
        if move not in board.legal_moves:
            return jsonify({"error": "Illegal move"}), 400
        
        board.push(move)
        
        # AI move
        if not board.is_game_over() and board.turn == game_state["ai_color"]:
            moves = list(board.legal_moves)
            if moves:
                ai_move = random.choice(moves)
                board.push(ai_move)
        
        return jsonify({
            "fen": board.fen(),
            "turn": "white" if board.turn == chess.WHITE else "black",
            "game_over": board.is_game_over(),
            "result": board.result() if board.is_game_over() else None
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiplayer')
def multiplayer():
    with open('multiplayer.html', 'r') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
