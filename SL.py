import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladder Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
player_pos = 1
dice_value = 1

# Snakes and Ladders dictionary
snakes_and_ladders = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

# Font
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_value = random.randint(1, 6)
                player_pos += dice_value
                if player_pos in snakes_and_ladders:
                    player_pos = snakes_and_ladders[player_pos]

    screen.fill(WHITE)
    
    # Draw the board
    for i in range(1, 101):
        row = (i - 1) // 10
        col = (i - 1) % 10
        x = col * (WIDTH // 10)
        if row % 2 == 0:
            x = WIDTH - x - (WIDTH // 10)
        y = row * (HEIGHT // 10)
        pygame.draw.rect(screen, GREEN if i % 2 == 0 else RED, (x, y, WIDTH // 10, HEIGHT // 10))
        
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(x + WIDTH // 20, y + HEIGHT // 20))
        screen.blit(text, text_rect)
        
        if i in snakes_and_ladders:
            dest = snakes_and_ladders[i]
            dest_row = 9 - (dest - 1) // 10
            dest_col = (dest - 1) % 10
            dest_x = dest_col * (WIDTH // 10) + (WIDTH // 20)
            if dest_row % 2 == 0:
                dest_x = WIDTH - dest_x
            dest_y = dest_row * (HEIGHT // 10) + (HEIGHT // 20)
            pygame.draw.line(screen, WHITE, (x + WIDTH // 20, y + HEIGHT // 20), (dest_x, dest_y), 3)

    # Draw player
    player_row = 9 - (player_pos - 1) // 10
    player_col = (player_pos - 1) % 10
    player_x = player_col * (WIDTH // 10) + (WIDTH // 20)
    if player_row % 2 == 0:
        player_x = WIDTH - player_x
    player_y = player_row * (HEIGHT // 10) + (HEIGHT // 20)
    pygame.draw.circle(screen, WHITE, (player_x, player_y), 20)

    # Display dice value
    dice_text = font.render(f"Dice: {dice_value}", True, RED)
    screen.blit(dice_text, (10, HEIGHT - 50))

    pygame.display.flip()

pygame.quit()
