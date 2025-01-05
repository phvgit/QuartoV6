from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from minimax import computer_move, best_move_for_piece
from match import Match
from game_over import game_over
import pygame

class GuiMainWin(Tk):
    def __init__(self, match):
        Tk.__init__(self)
        self.match = match
        self.title("Quarto")
        self.geometry("800x600")
        self.create_widgets()
        self.update_board()
        self.update_pieces()
        pygame.mixer.init()

    def create_widgets(self):
        self.canvas = Canvas(self, width=400, height=400)
        self.canvas.pack(pady=20, side=LEFT)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.info_label = Label(self, text="Your turn! Select a piece for the computer.")
        self.info_label.pack(pady=10)

        self.reset_button = Button(self, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.pieces_frame = Frame(self)
        self.pieces_frame.pack(pady=20, side=RIGHT)

        self.selected_piece_label = Label(self, text="Selected piece: None")
        self.selected_piece_label.pack(pady=10)

        self.computer_selected_piece_label = Label(self, text="Computer selected piece: None")
        self.computer_selected_piece_label.pack(pady=10)

        self.progress = ttk.Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress.pack(pady=10)

    def update_board(self):
        self.canvas.delete("all")
        for row in range(4):
            for col in range(4):
                x0 = col * 100
                y0 = row * 100
                x1 = x0 + 100
                y1 = y0 + 100
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")
                piece = self.match.board.get_piece(row, col)
                if piece:
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(piece))

    def update_pieces(self):
        for widget in self.pieces_frame.winfo_children():
            widget.destroy()

        for piece in self.match.board.unusedPieces():
            piece_button = Button(self.pieces_frame, text=str(piece), command=lambda p=piece: self.select_piece(p))
            piece_button.pack(pady=5)

    def select_piece(self, piece):
        self.match.selected_piece = piece
        self.selected_piece_label.config(text=f"Selected piece: {piece}")
        self.info_label.config(text="Computer's turn to place the piece.")
        self.play_sound("WoodWhoosh.wav")
        self.after(1000, self.computer_place_piece)

    def on_canvas_click(self, event):
        col = event.x // 100
        row = event.y // 100
        if self.match.board.is_position_empty(row, col):
            piece = self.match.selected_piece
            if piece:
                self.match.board.place_piece(piece, (row, col))
                self.match.selected_piece = None
                self.update_board()
                self.update_pieces()
                if game_over(self.match.board):
                    messagebox.showinfo("Game Over", "You win!")
                    self.reset_game()
                else:
                    self.info_label.config(text="Select a piece for the computer.")
                    self.match.is_human_turn = True

    def computer_place_piece(self):
        piece = self.match.selected_piece
        best_move = best_move_for_piece(self.match.board, piece, 3)
        self.match.board = best_move
        self.update_board()
        self.update_pieces()
        self.play_sound("WoodImpact.wav")
        if game_over(self.match.board):
            messagebox.showinfo("Game Over", "Computer wins!")
            self.reset_game()
        else:
            self.computer_select_piece()

    def computer_select_piece(self):
        self.progress.start()
        self.update_idletasks()
        _, piece_to_give = computer_move(self.match.board, 3)
        self.progress.stop()
        self.match.selected_piece = piece_to_give
        self.info_label.config(text="Your turn! Place the piece selected by the computer.")
        self.computer_selected_piece_label.config(text=f"Computer selected piece: {piece_to_give}")
        self.play_sound("WoodWhoosh.wav")

    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def reset_game(self):
        self.match.reset()
        self.update_board()
        self.update_pieces()
        self.info_label.config(text="Your turn! Select a piece for the computer.")
        self.selected_piece_label.config(text="Human selected piece: None")
        self.computer_selected_piece_label.config(text="Computer selected piece: None")

if __name__ == "__main__":
    match = Match()
    app = GuiMainWin(match)
    app.mainloop()