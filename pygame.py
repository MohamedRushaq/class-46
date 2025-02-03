import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Car Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Car properties
car_width = 50
car_height = 100
car_x = screen_width // 2 - car_width // 2  # Start in the middle
car_y = screen_height - car_height - 20  # A little above the bottom
car_speed = 5

# Obstacle properties
obstacle_width = 30
obstacle_height = 60
obstacle_speed = 7
obstacles = []  # List to store obstacles

# Game variables
score = 0
font = pygame.font.Font(None, 36)  # Default font
game_over = False

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to create new obstacles
def create_obstacle():
    x = random.randint(0, screen_width - obstacle_width)
    y = -obstacle_height  # Start above the screen
    obstacles.append([x, y])

# Game loop
running = True
obstacle_timer = 0  # Timer to control obstacle creation
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Car movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x -= car_speed
            if event.key == pygame.K_RIGHT:
                car_x += car_speed

    # Keep car within screen bounds
    if car_x < 0:
        car_x = 0
    elif car_x > screen_width - car_width:
        car_x = screen_width - car_width

    # Obstacle creation
    obstacle_timer += clock.get_rawtime()  # Time in milliseconds
    if obstacle_timer > 1500:  # Create obstacle every 1.5 seconds (adjust as needed)
        create_obstacle()
        obstacle_timer = 0

    # Move obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

        # Remove obstacles that go off-screen
        if obstacle[1] > screen_height:
            obstacles.remove(obstacle)
            score += 1  # Increment score when obstacle is passed

        # Collision detection
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if car_rect.colliderect(obstacle_rect):
            game_over = True

    # Draw everything
    screen.fill(white)  # White background

    # Draw car
    pygame.draw.rect(screen, black, (car_x, car_y, car_width, car_height))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # Display score
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

    # Game over screen
    if game_over:
        game_over_text = font.render("Game Over!", True, black)
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 20))
        pygame.display.flip()  # Update the display once to show "Game Over"
        pygame.time.delay(2000)  # Pause for 2 seconds
        running = False # Exit the game loop

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Control frame rate (60 FPS)

pygame.quit()