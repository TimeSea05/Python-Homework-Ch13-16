import sys
from random import randint
import pygame
from bullet import Bullet
from rect import Rect


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


def fire_bullets(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets, stats, play_button, rect):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, bullets,
                              ship, rect, mouse_x, mouse_y)


def update_screens(ai_settings, screen, ship, bullets, rect, play_button,
                   stats):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    rect.draw_rect()
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets, screen_rect, rect):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.right > screen_rect.right:
            bullets.remove(bullet)
    check_collision(bullets, rect)


def check_collision(bullets, rect):
    if pygame.sprite.spritecollideany(rect, bullets):
        list_collide = pygame.sprite.spritecollide(rect, bullets, True)
        rect.rect.y = 0
        rect.rect.x = randint(600, 850)


def check_play_button(ai_settings, screen, stats, play_button, bullets, ship,
                      rect, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats, rect, bullets, ship, ai_settings, screen)


def start_game(stats, rect, bullets, ship, ai_settings, screen):
    """开始游戏"""
    # 显示光标
    pygame.mouse.set_visible(True)
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 清空子弹列表
    bullets.empty()

    # 并让飞船居中
    ship.center_ship()

    rect.rect.y = 0


def check_missing_bullet(bullets, stats, screen_rect):
    for bullet in bullets:
        if bullet.rect.right == screen_rect.right:
            if stats.ships_left > 0:
                stats.ships_left -= 1
                break
            else:
                stats.game_active = False
