from board import Board

class Match:
    def __init__(self):
        self.board = Board()
        self.selected_piece = None
        self.is_human_turn = True

    def reset(self):
        self.board = Board()
        self.selected_piece = None
        self.is_human_turn = True