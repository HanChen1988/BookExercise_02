import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()  # 初始化背景设置，让Pygame能够正确地工作
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width
                                      , ai_settings.screen_height))
    # 创建一个名为screen的显示窗口
    # 实参（ai_settings.screen_width，ai_settings.screen_height）是一个元组
    # ，指定游戏窗口的尺寸。
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()  # 创建一个编组(group),用于存储所有有效的子弹,以便能够管理发射出去的
    # 所有子弹.这个编组将是pygame.sprite.Group类的一个实例;pygame.sprite.Group类似于列
    # 表,但提供了有助于开发游戏的额外功能.在主循环中,我们将使用这个编组在屏幕上绘制子弹,已经更
    # 新每个子弹的位置.

    # 创建一个外星人编组
    aliens = Group()  # 创建一个空编组,用于存储所有的外星人

    # 创建外星人人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 主循环检查玩家的输入
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船的位置
        ship.update()  # 飞船的位置将在检测到键盘事件后（但在更新屏幕前）更新。
        # 这样，玩家输入时，飞船的位置将更新，从而确保使用更新后的位置将飞船绘制到屏幕上。
        # 所有未消失的子弹的位置
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 我们使用更新后的位置来绘制新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # 修改对update_screen()的调用,让它能够访问外星人编组.


# 最后一行调用run_game()，这将初始化游戏并开始主循环
run_game()
