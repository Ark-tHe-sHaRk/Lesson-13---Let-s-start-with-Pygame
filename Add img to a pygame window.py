# Import the pygame library
import pygame

# Initialise pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Initialise display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Add img to a pygame window')

# Load and scale the Venom image
Venom_img = pygame.transform.scale(pygame.image.load('Venom.png'), (100, 100))
Venom_rect = Venom_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

# Initialise the font, render text and set text position
text = pygame.font.Font(None, 32).render('Venom', True, pygame.Color('Grey'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill((0, 0, 0))  # Fill the screen with black color
        display_surface.blit(Venom_img, Venom_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
    