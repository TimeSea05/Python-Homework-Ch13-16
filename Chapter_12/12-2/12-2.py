import sys
import pygame
from spongebob import SpongeBob


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    spongebob = SpongeBob(screen)
    pygame.display.set_caption("12-2")
    bg_color = (0, 0, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        spongebob.blitme()
        pygame.display.flip()


run_game()