from game_over import game_over

def select_next_piece(board, move):
    available_pieces = board.unusedPieces()
    best_piece = None
    min_opponent_winning_moves = float('inf')

    for piece in available_pieces:
        opponent_winning_moves = 0
        for pos in board.unusedPositions():
            new_board = move.copy()
            new_board.place_piece(piece, pos)
            if game_over(new_board):
                opponent_winning_moves += 1

        if opponent_winning_moves < min_opponent_winning_moves:
            min_opponent_winning_moves = opponent_winning_moves
            best_piece = piece

    return best_piece