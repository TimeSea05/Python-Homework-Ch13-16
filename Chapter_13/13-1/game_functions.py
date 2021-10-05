from star import Star


def get_number_x(star):
    rect_x = star.rect.x
    screen_x = star.screen_width
    number = (screen_x - 2 * rect_x) / (2 * rect_x)
    return int(number)


def create_fleet(stars, number, screen):
    default_star = Star(screen)
    for num in range(number):
        new_star = Star(screen)
        new_star.rect.x = default_star.rect.x + 2 * num * default_star.rect.x
        stars.add(new_star)