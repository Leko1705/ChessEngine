def evaluate(board) -> float:
    if board.white_mated(): return float('inf')
    if board.black_mated(): return -float('inf')
    if board.is_draw(): return 0

    pawnValue = 1
    knightValue = 3
    bishopValue = 3
    rookValue = 5
    queenValue = 9

    score = board.white_material() - board.black_material()
    score += board.white_material_adjustments()
    score -= board.black_material_adjustments()

    return score

# w -> s score = score - next(w) = (4)


def evaluate_paths(board, white_turn, depth=10) -> float:

    if depth == 0: return evaluate(board)
    score = None

    for move in board.legal_moves(white_turn):
        modified_board = board.apply_move(move)
        sub_score = evaluate_paths(modified_board, not white_turn, depth-1)

        if score is None:
            score = sub_score
        else:
            score = max(score, score - sub_score)

    return score


def minimax(board, depth) -> float:

    if board.game_over() or depth == 0:
        return evaluate(board)

    if board.turn == "white":
        best = -float('inf')
        for move in board.moves():
            board = board.make(move)
            val = minimax(board,depth-1)

            if val > best:
                best = val
    else:
        best = float('inf')
        for move in board.moves():
            board = board.make(move)
            val = minimax(board,depth-1)

            if val < best:
                best = val

    return best


