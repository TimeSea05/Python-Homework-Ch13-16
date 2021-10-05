from pygame.sprite import Sprite
from settings import Settings
import pygame


class Beam(Sprite):
    def __init__(self, screen, settings):
        super(Beam, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/beam.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self, settings):
        self.rect.y += settings.beam_drop_speed
