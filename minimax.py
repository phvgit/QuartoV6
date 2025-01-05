from game_over import game_over

def minimax(board, depth, is_maximizing, alpha, beta, piece_to_place):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_all_possible_moves(board, piece_to_place):
            next_piece = select_next_piece(board, move)
            eval = minimax(move, depth - 1, False, alpha, beta, next_piece)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_all_possible_moves(board, piece_to_place):
            next_piece = select_next_piece(board, move)
            eval = minimax(move, depth - 1, True, alpha, beta, next_piece)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def computer_move(board, depth):
    best_move = None
    best_piece_to_give = None
    max_eval = float('-inf')
    available_pieces = board.unusedPieces()

    for piece in available_pieces:
        for move in get_all_possible_moves(board, piece):
            next_piece = select_next_piece(board, move)
            eval = minimax(move, depth, False, float('-inf'), float('inf'), next_piece)
            if eval > max_eval:
                max_eval = eval
                best_move = move
                best_piece_to_give = next_piece

    return best_move, best_piece_to_give

def best_move_for_piece(board, piece, depth):
    best_move = None
    max_eval = float('-inf')

    for move in get_all_possible_moves(board, piece):
        eval = minimax(move, depth, False, float('-inf'), float('inf'), None)
        if eval > max_eval:
            max_eval = eval
            best_move = move

    return best_move

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

def get_all_possible_moves(board, piece_to_place):
    possible_moves = []
    available_positions = board.unusedPositions()

    for pos in available_positions:
        new_board = board.copy()
        new_board.place_piece(piece_to_place, pos)
        possible_moves.append(new_board)

    return possible_moves

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