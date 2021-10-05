import sys
import pygame


def check_keydown_events(event, patrick):
    if event.key == pygame.K_LEFT:
        patrick.moving_left = True
    elif event.key == pygame.K_RIGHT:
        patrick.moving_right = True


def check_keyup_events(event, patrick):
    if event.key == pygame.K_LEFT:
        patrick.moving_left = False
    elif event.key == pygame.K_RIGHT:
        patrick.moving_right = False


def check_events(patrick):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, patrick)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, patrick)


def update_screens(settings, screen, patrick, ball):
    screen.fill(settings.bg_color)
    patrick.blitme()
    ball.blitme()
    pygame.display.flip()


def check_ball_bottom(settings, ball):
    if ball.rect.bottom == settings.screen_height:
        settings.missing_times += 1
    if settings.missing_times >= 3:
        print("You Lose")
        sys.exit()
