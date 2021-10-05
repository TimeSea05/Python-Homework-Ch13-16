import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from star import Star
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("13-1")

    star = Star(screen)
    stars = Group()
    default_x = star.rect.x
    number = gf.get_number_x(star)
    gf.create_fleet(stars, number, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(settings.bg_color)
            stars.draw(screen)
            pygame.display.flip()


if __name__ == "__main__":
    run_game()
