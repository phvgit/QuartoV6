def evaluate(board):
    def check_line(line):
        if len(line) != 4 or any(piece is None for piece in line):
            return 0
        attributes = ['height', 'color', 'shape', 'consistency']
        score = 0
        for attr in attributes:
            if all(getattr(piece, attr) == getattr(line[0], attr) for piece in line):
                score += 1
        return score

    total_score = 0

    # Check rows
    for row in range(4):
        line = [board.get_piece(row, col) for col in range(4)]
        total_score += check_line(line)

    # Check columns
    for col in range(4):
        line = [board.get_piece(row, col) for row in range(4)]
        total_score += check_line(line)

    # Check diagonals
    diagonal1 = [board.get_piece(i, i) for i in range(4)]
    diagonal2 = [board.get_piece(i, 3 - i) for i in range(4)]
    total_score += check_line(diagonal1)
    total_score += check_line(diagonal2)

    return total_score