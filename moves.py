def get_all_possible_moves(board, piece_to_place):
    possible_moves = []
    available_positions = board.unusedPositions()

    for pos in available_positions:
        new_board = board.copy()
        new_board.place_piece(piece_to_place, pos)
        possible_moves.append(new_board)

    return possible_moves