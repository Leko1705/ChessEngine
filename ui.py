import pygame

import engine


# Init Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
LIGHT_COLOR = (255,255,255) # White
DARK_COLOR = (0,0,0) # Black
SQUARE_SIZE = WIDTH // 8

# Set up the display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess Board")

# Load images
white_king = pygame.image.load("res/piece_white_king.png").convert_alpha()
white_queen = pygame.image.load("res/piece_white_queen.png").convert_alpha()
white_bishop = pygame.image.load("res/piece_white_bishop.png").convert_alpha()
white_knight = pygame.image.load("res/piece_white_knight.png").convert_alpha()
white_rook = pygame.image.load("res/piece_white_rook.png").convert_alpha()
white_pawn = pygame.image.load("res/piece_white_pawn.png").convert_alpha()

black_king = pygame.image.load("res/piece_black_king.png").convert_alpha()
black_queen = pygame.image.load("res/piece_black_queen.png").convert_alpha()
black_bishop = pygame.image.load("res/piece_black_bishop.png").convert_alpha()
black_knight = pygame.image.load("res/piece_black_knight.png").convert_alpha()
black_rook = pygame.image.load("res/piece_black_rook.png").convert_alpha()
black_pawn = pygame.image.load("res/piece_black_pawn.png").convert_alpha()

# Scale all pieces to the defined square size
WHITE_KING = pygame.transform.scale(white_king, (SQUARE_SIZE, SQUARE_SIZE))
WHITE_QUEEN = pygame.transform.scale(white_queen, (SQUARE_SIZE, SQUARE_SIZE))
WHITE_BISHOP = pygame.transform.scale(white_bishop, (SQUARE_SIZE, SQUARE_SIZE))
WHITE_KNIGHT = pygame.transform.scale(white_knight, (SQUARE_SIZE, SQUARE_SIZE))
WHITE_ROOK = pygame.transform.scale(white_rook, (SQUARE_SIZE, SQUARE_SIZE))
WHITE_PAWN = pygame.transform.scale(white_pawn, (SQUARE_SIZE, SQUARE_SIZE))

BLACK_KING = pygame.transform.scale(black_king, (SQUARE_SIZE, SQUARE_SIZE))
BLACK_QUEEN = pygame.transform.scale(black_queen, (SQUARE_SIZE, SQUARE_SIZE))
BLACK_BISHOP = pygame.transform.scale(black_bishop, (SQUARE_SIZE, SQUARE_SIZE))
BLACK_KNIGHT = pygame.transform.scale(black_knight, (SQUARE_SIZE, SQUARE_SIZE))
BLACK_ROOK = pygame.transform.scale(black_rook, (SQUARE_SIZE, SQUARE_SIZE))
BLACK_PAWN = pygame.transform.scale(black_pawn, (SQUARE_SIZE, SQUARE_SIZE))



class UI:

    def __init__(self):
        self.state_changed = False
        self.tile_click_listener = None


    def set_tile_click_listener(self, function: callable):
        """
        Binds a function to the ui in such a way that it is
        called whenever a tile is clicked. The callable is
        of the form:

        def callable(x, y):
            # code here
            pass
        :param function:
        :return: None
        """
        self.tile_click_listener = function


    def start(self, state: engine.State):
        self.state_changed = True  # enforce initial paint

        # Main loop to keep the window open
        while state.running:

            self.process_events(state)

            # TODO add mouse event listening logic (notifying self.tile_click_listener)

            if self.state_changed:
                self.create_graphic_board()
                self.draw_pieces_from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
                pygame.display.flip()
                self.state_changed = False

        # Quit Pygame
        pygame.quit()


    def notify_state_changed(self):
        """
        Notifies the UI that the state has changed and updated it
        accordingly.
        """
        self.state_changed = True


    @staticmethod
    def process_events(state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.running = False


    @staticmethod
    def create_graphic_board() -> None:

        for file in range(8):
            for rank in range(8):
                is_light_square = (file + rank) % 2 != 0
                square_color = LIGHT_COLOR if is_light_square else DARK_COLOR
                position = (file * SQUARE_SIZE, rank * SQUARE_SIZE)
                pygame.draw.rect(screen,square_color,(position[0],position[1],SQUARE_SIZE,SQUARE_SIZE))


    @staticmethod
    def draw_pieces_from_fen(fen: str) -> None:
        piece_map = {
            'K': white_king, 'Q': white_queen, 'B': white_bishop,
            'N': white_knight, 'R': white_rook, 'P': white_pawn,
            'k': black_king, 'q': black_queen, 'b': black_bishop,
            'n': black_knight, 'r': black_rook, 'p': black_pawn
        }

        # Split the FEN string to get the board state
        board_state = fen.split()[0]
        ranks = board_state.split('/')

        for rank_index, rank in enumerate(ranks):
            file_index = 0
            for char in rank:
                if char.isdigit():
                    file_index += int(char)  # Skip empty squares
                else:
                    screen.blit(piece_map[char], (file_index * SQUARE_SIZE, (7 - rank_index) * SQUARE_SIZE))
                    file_index += 1

