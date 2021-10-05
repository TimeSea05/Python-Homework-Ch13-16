from beam import Beam


def get_number_x(settings, beam):
    screen_width = settings.screen_width
    image_width = beam.rect.width
    number_x = (screen_width - image_width) / (2 * image_width)
    return int(number_x)


def get_number_y(settings, beam):
    screen_height = settings.screen_height
    image_height = beam.rect.height
    number_y = (screen_height - 2 * image_height) / (2 * image_height)
    return int(number_y)


def create_fleet(beams, settings, screen):
    beam = Beam(screen, settings)
    number_x = get_number_x(settings, beam)
    number_y = get_number_y(settings, beam)
    rect_x = beam.rect.width
    rect_y = beam.rect.height
    for num_x in range(number_x):
        for num_y in range(number_y):
            new_beam = Beam(screen, settings)
            new_beam.rect.x = (2 * num_x + 1) * rect_x
            new_beam.rect.y = (2 * num_y + 1) * rect_y
            beams.add(new_beam)


"""
def add_a_line_fleet(beams, settings, screen):
    beam = Beam(screen, settings)
    number_x = get_number_x(settings, beam)
    rect_x = beam.rect.width
    for num_x in range(number_x):
        new_beam = Beam(screen, settings)
        new_beam.rect.x = (2 * num_x + 1) * rect_x
        beams.add(new_beam)
"""


def check_edge(beams, settings, screen):
    default_beam = Beam(screen, settings)
    for beam in beams.copy():
        if beam.rect.y >= settings.screen_height:
            beam.rect.y = default_beam.rect.y
