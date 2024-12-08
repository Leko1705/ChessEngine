

def pos_to_board(x, y):
    return y*8 + x

def board_to_pos(board):
    return board % 8, board // 8

def is_valid_position(x, y):
    return 0 <= pos_to_board(x, y) <= (2**63)

def put_piece(x, y):
    return board | pos_to_board(x, y)

def remove_piece(x, y):
    return board & ~(1 << pos_to_board(x, y))

def board():
    return team_white() | team_black()

def team_white():
    return white_king | white_queen | white_rook | white_bishop | white_knight | white_pawn

def team_black():
    return black_king | black_queen | black_rook | black_bishop | black_knight | black_pawn

def all_pawns():
    return black_pawn | white_pawn

def all_bishops():
    return black_bishop | white_bishop

def all_knights():
    return black_knight | white_knight

def all_rooks():
    return black_rook | white_rook

def all_queens():
    return black_queen | white_queen

def king_moves(x: int, y: int):
    moves = 0
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            moves |= pos_to_board(x+dx, y+dy)
    return moves

def queen_moves(x: int, y: int):
    moves = 0
    for dx in range(-7, 8):
        for dy in range(-7, 8):
            if abs(dx) == abs(dy) | dx == 0 | dy == 0:
                moves |= pos_to_board(x + dx, y + dy)
    return moves

def rook_moves(x: int, y: int):
    moves = 0
    for dx in range(-7, 8):
        if dx != 0:
            moves |= pos_to_board(x + dx, y) | pos_to_board(x, y + dx)
    return moves


def bishop_moves(x: int, y: int):
    moves = 0
    # Diagonal directions: top-right, top-left, bottom-right, bottom-left
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dx, dy in directions:
        for step in range(1, 8):  # Move up to 7 squares in each direction
            move_x = x + dx * step
            move_y = y + dy * step
            if not is_valid_position(move_x, move_y):
                moves |= pos_to_board(move_x, move_y)
            else:
                break  # Stop if we go out of bounds
    return moves

def knight_moves(x: int, y: int):
    moves = 0
    knight_moves_offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                            (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for dx, dy in knight_moves_offsets:
        moves |= pos_to_board(x + dx, y + dy)
    return moves

def pawn_moves(x: int, y: int, white: bool):
    moves = 0

    start_pos = 1 if white else 6
    direction = 1 if white else -1

    if y == start_pos:  # Starting position
        moves |= pos_to_board(x, y + (direction * 2))
    moves |= pos_to_board(x, y + direction)  # Move forward one square

    return moves

def pawn_captures(x: int, y: int, white: bool):
    direction = 1 if white else -1

    moves = pos_to_board(x - 1, y + direction)  # Capture diagonally left
    moves |= pos_to_board(x + 1, y + direction)  # Capture diagonally right

    return moves

def is_black(x: int, y: int):
    return (team_black() and pos_to_board(x, y)) != 0

def is_white(x: int, y: int):
    return (team_white() and pos_to_board(x, y)) != 0

def is_king(x: int, y: int):
    return (white_king | black_king) and pos_to_board(x, y)

def is_queen(x: int, y: int):
    return (white_queen | black_queen) and pos_to_board(x, y)

def is_rook(x: int, y: int):
    return (white_rook | black_rook) and pos_to_board(x, y)

def is_bishop(x: int, y: int):
    return (white_bishop | black_bishop) and pos_to_board(x, y)

def is_knight(x: int, y: int):
    return (white_knight | black_knight) and pos_to_board(x, y)

def is_pawn(x: int, y: int):
    return (white_pawn | black_pawn) and pos_to_board(x, y)

def white_moves():
    """
    Returns list of Moves for all left pieces of the white team
    :return: Moves of all left white pieces
    """
    #  TODO impl me
    pass

def black_moves():
    """
    Returns list of Moves for all left pieces of the black team
    :return: Moves of all left black pieces
    """
    #  TODO impl me
    pass

class State:

    def __init__(self):

        # Runtime variables
        self.turn = "white"
        self.selected = None

        # Termination variables
        self.running = True
        self.result = None


class Move:

    def __init__(self, applier, inverter):
        self.applier = applier
        self.inverter = inverter

    def apply(self):
        self.applier()

    def invert(self):
        self.inverter()



# initialize positions

black_king = pos_to_board(3, 7)
white_king = pos_to_board(3, 0)

black_queen = pos_to_board(4, 7)
white_queen = pos_to_board(4, 0)

black_rook = pos_to_board(0, 7) | pos_to_board(7, 7)
white_rook = pos_to_board(0, 0) | pos_to_board(7, 0)

black_bishop = pos_to_board(2, 7) | pos_to_board(5, 7)
white_bishop = pos_to_board(2, 0) | pos_to_board(5, 0)

black_knight = pos_to_board(1, 7) | pos_to_board(6, 7)
white_knight = pos_to_board(1, 0) | pos_to_board(6, 0)

black_pawn = 0
white_pawn = 0

for i in range(0, 8):
    black_pawn |= pos_to_board(i, 6)
    white_pawn |= pos_to_board(i, 1)