import chess
import tkinter as tk
from tkinter import messagebox
import random

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = chess.Board()
        self.selected_square = None
        
        # Full screen setup
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.square_size = min(screen_width // 8, (screen_height - 50) // 8)
        canvas_width = self.square_size * 8
        canvas_height = self.square_size * 8
        
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        
        self.piece_symbols = {
            'P': '♙', 'p': '♟',
            'R': '♖', 'r': '♜',
            'N': '♘', 'n': '♞',
            'B': '♗', 'b': '♝',
            'Q': '♕', 'q': '♛',
            'K': '♔', 'k': '♚'
        }
        self.ai_color = chess.BLACK  # AI plays as black
        self.draw_board()
        self.status_label = tk.Label(root, text="White to move")
        self.status_label.pack()

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["#f0d9b5", "#b58863"]
        for row in range(8):
            for col in range(8):
                x1, y1 = col * self.square_size, row * self.square_size
                x2, y2 = x1 + self.square_size, y1 + self.square_size
                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                piece = self.board.piece_at(chess.square(col, 7 - row))
                if piece:
                    symbol = self.piece_symbols.get(piece.symbol(), piece.symbol())
                    font_size = int(self.square_size * 0.6)
                    self.canvas.create_text(x1 + self.square_size // 2, y1 + self.square_size // 2, text=symbol, font=("Arial", font_size))
        
        # Highlight selected square
        if self.selected_square is not None:
            col = chess.square_file(self.selected_square)
            row = 7 - chess.square_rank(self.selected_square)
            x1, y1 = col * self.square_size, row * self.square_size
            x2, y2 = x1 + self.square_size, y1 + self.square_size
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=3)
            
            # Show possible moves with dots
            for move in self.board.legal_moves:
                if move.from_square == self.selected_square:
                    col_to = chess.square_file(move.to_square)
                    row_to = 7 - chess.square_rank(move.to_square)
                    x = col_to * self.square_size + self.square_size // 2
                    y = row_to * self.square_size + self.square_size // 2
                    if self.board.is_capture(move):
                        # Red dot for captures
                        radius = int(self.square_size * 0.15)
                        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")
                    else:
                        # Green dot for moves
                        radius = int(self.square_size * 0.1)
                        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="green")

    def on_click(self, event):
        col = event.x // self.square_size
        row = 7 - (event.y // self.square_size)
        square = chess.square(col, row)
        if self.selected_square is None:
            if self.board.piece_at(square) and self.board.color_at(square) == self.board.turn:
                self.selected_square = square
                self.draw_board()
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.draw_board()
                self.update_status()
                if self.board.is_game_over():
                    self.game_over()
                elif self.board.turn == self.ai_color:
                    self.root.after(500, self.make_ai_move)  # Delay AI move for better UX
            else:
                self.selected_square = None
                self.draw_board()

    def make_ai_move(self):
        moves = list(self.board.legal_moves)
        if moves:
            move = random.choice(moves)
            self.board.push(move)
            self.draw_board()
            self.update_status()
            if self.board.is_game_over():
                self.game_over()

    def update_status(self):
        turn = "White" if self.board.turn else "Black"
        self.status_label.config(text=f"{turn} to move")

    def game_over(self):
        result = self.board.result()
        messagebox.showinfo("Game Over", f"Result: {result}")

def main():
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()