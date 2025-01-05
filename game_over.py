def game_over(board):
    def check_line(line):
        if len(line) != 4 or any(piece is None for piece in line):
            return False
        attributes = ['height', 'color', 'shape', 'consistency']
        for attr in attributes:
            if all(getattr(piece, attr) == getattr(line[0], attr) for piece in line):
                return True
        return False

    # Check rows
    for row in range(4):
        line = [board.get_piece(row, col) for col in range(4)]
        if check_line(line):
            return True

    # Check columns
    for col in range(4):
        line = [board.get_piece(row, col) for row in range(4)]
        if check_line(line):
            return True

    # Check diagonals
    diagonal1 = [board.get_piece(i, i) for i in range(4)]
    diagonal2 = [board.get_piece(i, 3 - i) for i in range(4)]
    if check_line(diagonal1) or check_line(diagonal2):
        return True

    return False