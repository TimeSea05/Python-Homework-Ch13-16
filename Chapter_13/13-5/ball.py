import pygame
from random import randint
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, screen, settings):
        super(Ball, self).__init__()
        self.image = pygame.image.load("images/Ball.bmp")
        self.settings = settings
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect.x = randint(50, 1150)
        self.rect.y = self.rect.height

    def update(self):
        self.rect.y += 1
        if self.rect.y >= self.settings.screen_height:
            self.rect.y = 0
            self.rect.x = randint(50, 1150)

    def disappear(self):
        self.rect.y = 0
        self.rect.x = randint(50, 1150)

    def blitme(self):
        self.screen.blit(self.image, self.rect)