import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from button import Button
from game_stats import GameStats
from rect import Rect


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("14-2")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    # 创建一个按钮
    button = Button(ai_settings, screen, "Play")
    # 创建游戏信息统计实例
    stats = GameStats(ai_settings)
    # 创建矩形
    rect = Rect(ai_settings, screen)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, button,
                        rect)
        if stats.game_active:
            ship.update()
            rect.update()
            gf.update_bullets(bullets, screen.get_rect(), rect)
            gf.check_missing_bullet(bullets, stats, screen.get_rect())
        gf.update_screens(ai_settings, screen, ship, bullets, rect, button,
                          stats)


run_game()
