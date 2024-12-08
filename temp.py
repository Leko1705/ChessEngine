from main import board


class Piece:
    EMPTY = 0
    KING = 1
    PAWN = 2
    KNIGHT = 3
    BISHOP = 4
    ROOK = 5
    QUEEN = 6

    WHITE = 8
    BLACK = 16


class Board:

    def __init__(self):
        self.squares: list[int] = [0 for _ in range(64)]

    def board(self):
        self.squares[0] = Piece.WHITE or Piece.BISHOP