import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SQUARE_SIZE = WIDTH // 8

# Chess board representation
chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Selected piece
selected_piece = None
selected_row, selected_col = None, None

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked_col = event.pos[0] // SQUARE_SIZE
            clicked_row = event.pos[1] // SQUARE_SIZE

            if selected_piece is None:
                piece = chess_board[clicked_row][clicked_col]
                if piece != ' ':
                    selected_piece = piece
                    selected_row, selected_col = clicked_row, clicked_col
            else:
                chess_board[selected_row][selected_col] = ' '
                chess_board[clicked_row][clicked_col] = selected_piece
                selected_piece = None

    # Draw chess board
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            piece = chess_board[row][col]
            if piece != ' ':
                font = pygame.font.Font(None, 60)
                text = font.render(piece, True, (0, 0, 0))
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                  row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
