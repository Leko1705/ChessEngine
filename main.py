import engine
import ui


def handle_piece_selection(x, y):
    if state.turn == "white" and engine.is_white(x, y):
        state.selected = (x, y)
    elif state.turn == "black" and engine.is_black(x, y):
        state.selected = (x, y)


def perform_move(from_pos: tuple[int, int], to_pos):
    if state.turn == "white" and engine.is_white(*to_pos): return False  # cannot take team member
    if state.turn == "black" and engine.is_black(*to_pos): return False

    remove_bitshift = engine.pos_to_board(*from_pos)

    if engine.is_king(*from_pos) and (engine.king_moves(*state.selected) & to_pos) != 0:
        if (engine.white_king & to_pos) != 0:
            engine.white_king |= to_pos
            engine.white_king &= ~(1 << remove_bitshift)
        else:
            engine.black_king |= to_pos
            engine.black_king &= ~(1 << remove_bitshift)
        return True

    if engine.is_queen(*from_pos) and (engine.queen_moves(*state.selected) & to_pos) != 0:
        if (engine.white_queen & to_pos) != 0:
            engine.white_queen |= to_pos
            engine.white_queen &= ~(1 << remove_bitshift)
        else:
            engine.black_queen |= to_pos
            engine.black_queen &= ~(1 << remove_bitshift)
        return True

    if engine.is_rook(*from_pos) and (engine.rook_moves(*state.selected) & to_pos) != 0:
        if (engine.white_rook & to_pos) != 0:
            engine.white_rook |= to_pos
            engine.white_rook &= ~(1 << remove_bitshift)
        else:
            engine.black_rook |= to_pos
            engine.black_rook &= ~(1 << remove_bitshift)
        return True

    if engine.is_bishop(*from_pos) and (engine.bishop_moves(*state.selected) & to_pos) != 0:
        if (engine.white_bishop & to_pos) != 0:
            engine.white_bishop |= to_pos
            engine.white_bishop &= ~(1 << remove_bitshift)
        else:
            engine.black_bishop |= to_pos
            engine.black_bishop &= ~(1 << remove_bitshift)
        return True

    if engine.is_knight(*from_pos) and (engine.knight_moves(*state.selected) & to_pos) != 0:
        if (engine.white_knight & to_pos) != 0:
            engine.white_knight |= to_pos
            engine.white_knight &= ~(1 <<remove_bitshift)
        else:
            engine.black_knight |= to_pos
            engine.black_knight &= ~(1 << remove_bitshift)
        return True

    if engine.is_pawn(*from_pos):
        x = state.selected[0]
        y = state.selected[1]
        white_turn = (state.turn == "white")
        moves = engine.pawn_moves(x, y, white_turn) | engine.pawn_captures(x, y, white_turn)

        if white_turn and ((moves & to_pos) != 0):
            engine.white_pawn |= to_pos
            engine.white_pawn &= ~(1 << remove_bitshift)
            return True

        elif not white_turn and ((moves & to_pos) != 0):
            engine.black_pawn |= to_pos
            engine.black_pawn &= ~(1 << remove_bitshift)
            return True

    return False


def in_check(team):
    # TODO impl me
    pass


def check_termination():
    has_next_move = False

    if state.turn == "white":
        next_player = "black"
        next_moves = engine.black_moves()
        winner_candidate = "White"
    else:
        next_player = "white"
        next_moves = engine.white_moves()
        winner_candidate = "Black"

    for move in next_moves:
        move.apply()
        has_next_move = not in_check(next_player)
        move.invert()
        if has_next_move: break

    if not has_next_move:
        state.running = False
        if in_check(next_player):
            state.result = f"{winner_candidate} wins!"
            return
        else:
            state.result = "Draw!"


def handle_move(x, y):
    target = engine.pos_to_board(x, y)

    if perform_move(state.selected, target):
        ui.notify_state_changed()

    state.selected = None
    check_termination()


def tile_click_listener(x, y):
    if state.selected is None:
        handle_piece_selection(x, y)
    else:
        handle_move(x, y)


if __name__ == '__main__':
    state = engine.State()
    ui = ui.UI()
    ui.set_tile_click_listener(tile_click_listener)
    ui.start(state)