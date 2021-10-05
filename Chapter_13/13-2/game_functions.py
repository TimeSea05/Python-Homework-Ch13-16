from random import randint
from star import Star


def create_fleet(stars, screen, number, settings):
    star = Star(screen)
    rect_x = star.rect.x
    rect_y = star.rect.y

    for num in range(number):
        new_star = Star(screen)
        random_x = randint(0, 12)
        random_y = randint(0, 8)
        new_star.rect.x = (1 + random_x) * rect_x
        new_star.rect.y = (1 + random_y) * rect_y
        if new_star.rect.x < settings.screen_width and new_star.rect.y < settings.screen_height:
            stars.add(new_star)