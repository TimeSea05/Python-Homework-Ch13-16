import pygame
from pygame.sprite import Sprite


class Patrick(Sprite):
    def __init__(self, screen):
        super(Patrick, self).__init__()
        self.image = pygame.image.load("images/Patrick.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)