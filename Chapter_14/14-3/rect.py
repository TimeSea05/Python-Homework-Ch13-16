import pygame
from pygame.sprite import Sprite


class Rect(Sprite):
    def __init__(self, ai_settings, screen):
        super(Rect, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.rect = pygame.Rect(600, 0, 30, 200)
        self.color = (0, 0, 0)
        self.speed_factor = self.ai_settings.rect_speed_factor
        # 1 代表向下， -1 代表向下
        self.direction = 1

    def update(self):
        self.speed_factor = self.ai_settings.rect_speed_factor
        if self.rect.bottom >= self.ai_settings.screen_height:
            self.direction = -1
        if self.rect.top <= 0:
            self.direction = 1
        self.rect.y += self.direction * self.speed_factor

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect)