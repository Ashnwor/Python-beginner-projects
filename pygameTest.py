import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("pygame test")
# SET UP COLORS:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    font = pygame.font.SysFont(None,36)
    text = font.render('Hello motherfucker!', True, WHITE, BLACK)
    textRectangle = text.getRect()
    textRectangle.centerx = window.getRect().centerx
    textRectangle.centery = window.getRect().centery

    # Main game loop
    while True:

        # Quit the game if QUIT is initiated
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

main()