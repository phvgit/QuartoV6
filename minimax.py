from evaluate import evaluate
from game_over import game_over
from moves import get_all_possible_moves
from select_next_piece import select_next_piece

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