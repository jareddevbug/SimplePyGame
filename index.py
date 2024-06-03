import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the Square")

# Colors
background_color = (0, 0, 0)  # Black
square_color = (255, 0, 0)    # Red

# Square properties
square_size = 50
x, y = 375, 275  # Starting position in the center of the screen

# Movement speed
speed = 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the set of keys currently being pressed
    keys = pygame.key.get_pressed()

    # Move the square based on the keys pressed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Keep the square within the screen boundaries
    if x < 0:
        x = 0
    if x > 800 - square_size:
        x = 800 - square_size
    if y < 0:
        y = 0
    if y > 600 - square_size:
        y = 600 - square_size

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the square
    pygame.draw.rect(screen, square_color, (x, y, square_size, square_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
