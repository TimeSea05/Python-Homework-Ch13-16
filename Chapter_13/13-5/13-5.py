import pygame
import sys
from ball import Ball
from patrick import Patrick
from settings import Settings
import game_functions as gf
from pygame.sprite import Sprite


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("13-5")

    ball = Ball(screen, settings)
    patrick = Patrick(screen)

    while True:
        gf.check_events(patrick)
        patrick.update()
        ball.update()
        if pygame.sprite.collide_rect(patrick, ball):
            ball.disappear()
        gf.update_screens(settings, screen, patrick, ball)


run_game()
