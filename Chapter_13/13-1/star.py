from pygame.sprite import Sprite
import pygame


class Star(Sprite):
    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height