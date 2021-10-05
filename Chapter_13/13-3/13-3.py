import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from settings import Settings
from beam import Beam
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("13-3")
    beams = Group()
    gf.create_fleet(beams, settings, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(settings.bg_color)
        beams.update(settings)
        gf.check_edge(beams, settings)
        beams.draw(screen)
        pygame.display.flip()
        if len(beams) == 0:
            sys.exit()


if __name__ == "__main__":
    run_game()
