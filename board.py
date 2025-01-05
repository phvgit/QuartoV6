class Board:
    def __init__(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]
        self.unused_pieces = self.initialize_pieces()

    def initialize_pieces(self):
        pieces = []
        for height in [0, 1]:
            for color in [0, 1]:
                for shape in [0, 1]:
                    for consistency in [0, 1]:
                        pieces.append(Piece(height, color, shape, consistency))
        return pieces

    def get_piece(self, row, col):
        return self.grid[row][col]

    def place_piece(self, piece, position):
        row, col = position
        self.grid[row][col] = piece
        if piece in self.unused_pieces:
            self.unused_pieces.remove(piece)

    def is_position_empty(self, row, col):
        return self.grid[row][col] is None

    def unusedPositions(self):
        positions = []
        for row in range(4):
            for col in range(4):
                if self.is_position_empty(row, col):
                    positions.append((row, col))
        return positions

    def unusedPieces(self):
        return self.unused_pieces

    def copy(self):
        new_board = Board()
        new_board.grid = [row[:] for row in self.grid]
        new_board.unused_pieces = self.unused_pieces[:]
        return new_board

class Piece:
    def __init__(self, height, color, shape, consistency):
        self.height = height
        self.color = color
        self.shape = shape
        self.consistency = consistency

    def __str__(self):
        return f"{self.height}{self.color}{self.shape}{self.consistency}"