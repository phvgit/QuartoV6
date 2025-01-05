from board import Board

class Match:
    def __init__(self):
        self.board = Board()
        self.selected_piece = None
        self.is_human_turn = True
        self.numMove = 1

    def reset(self):
        self.board = Board()
        self.selected_piece = None
        self.is_human_turn = True
        self.numMove = 1