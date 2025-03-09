import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse Click Speed Test")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
clicks = 0
time_left = 10
timer_started = False  # Track if the timer has started
clock = pygame.time.Clock()

# Set up game states
START_SCREEN = "start"
GAME_SCREEN = "game"
GAME_OVER_SCREEN = "game_over"
current_screen = START_SCREEN

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and current_screen == GAME_SCREEN:
            if not timer_started:
                timer_started = True
            elif timer_started:
                clicks += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current_screen == START_SCREEN:
                current_screen = GAME_SCREEN
                clicks = 0
                time_left = 10
            elif event.key == pygame.K_SPACE and current_screen == GAME_OVER_SCREEN:
                current_screen = START_SCREEN
                timer_started = False  # Reset the timer status

    display.fill(WHITE)
    
    if current_screen == START_SCREEN:
        # Display start screen
        start_text = font.render("Click SPACE to start", True, BLACK)
        display.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2 - start_text.get_height() // 2))
    elif current_screen == GAME_SCREEN:
        # Display countdown timer
        if timer_started:
            time_left -= clock.tick_busy_loop(60) / 1000
        timer_text = font.render(f"Time Left: {max(time_left, 0):.2f} s", True, BLACK)
        display.blit(timer_text, (20, 20))
        pygame.draw.circle(display, BLACK, (width // 2, height // 2), 50)
        if time_left <= 0:
            current_screen = GAME_OVER_SCREEN
    elif current_screen == GAME_OVER_SCREEN:
        # Display game over screen with score
        score_text = font.render(f"Clicks: {clicks}", True, BLACK)
        display.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2))
        pygame.draw.rect(display, BLACK, (width // 2 - 100, height // 2 + 50, 200, 50))
        play_again_text = font.render("Play Again (SPACE)", True, WHITE)
        display.blit(play_again_text, (width // 2 - play_again_text.get_width() // 2, height // 2 + 50))

    pygame.display.flip()

pygame.quit()