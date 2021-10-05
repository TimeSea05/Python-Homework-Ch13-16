import pygame
from rocket_settings import Settings
import game_functions as gf
from rocket import Rocket


def run_game():
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode(
        (r_settings.screen_width, r_settings.screen_height))
    rocket = Rocket(screen)
    pygame.display.set_caption("12-3")

    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screens(r_settings, screen, rocket)


run_game()
