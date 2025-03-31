# Importing necessary modules
import pygame

# Initialising required modules
pygame.init()

# Setting up window geometry
screen = pygame.display.set_mode((500, 500))

# Setting up the title of the window
pygame.display.set_caption('My First Game Screen')

# Adding an image to the window
image = pygame.image.load("Venom.png")
image = pygame.transform.scale(image, (300, 300))

# Calculate the position to center the image
image_rect = image.get_rect(center=(500 // 2, 500 // 2))

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Setting up the background color and drawing the image
    screen.fill((128, 128, 128))
    screen.blit(image, image_rect.topleft)
    pygame.display.flip()

# Quit pygame
pygame.quit()