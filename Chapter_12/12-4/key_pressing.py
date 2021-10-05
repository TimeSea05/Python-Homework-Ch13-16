import pygame
import sys


def set_position(textsurface, screen_rect):
    textrect = textsurface.get_rect()
    textrect.centerx = screen_rect.centerx
    textrect.centery = screen_rect.centery
    return textrect


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("12-4")
    screen_rect = screen.get_rect()

    text = 'Ready? Go!'
    textsurface = pygame.font.Font('C:\\Windows\\Fonts\\simfang.ttf',
                                   88).render(text, True, (255, 0, 0))
    text_rect = set_position(textsurface, screen_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                text = str(event.key)
                textsurface = pygame.font.Font(
                    'C:\\Windows\\Fonts\\simfang.ttf',
                    88).render(text, True, (255, 0, 0))
                textrect = set_position(textsurface, screen_rect)

            screen.fill((255, 255, 255))
            screen.blit(textsurface, text_rect)
            pygame.display.flip()


run_game()
