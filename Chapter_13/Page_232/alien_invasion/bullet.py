import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width
                                , ai_settings.bullet_height)  # 我们创建了子弹的属
        # 性rect.子弹并非基于图像的，因此我们必须使用pygame.Rect()类从空白开始创建一个矩形。
        # 创建这个类的实例时，必须提供矩形左上角的x坐标和y坐标,还有矩形的宽度和高度.
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top  # 子弹应该从飞船顶部射出,因此我们将表示子弹的
        # rect的top属性设置为飞船的rect的top属性,让子弹看起来像是从飞船中射出的.

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):  # 方法update()管理子弹的位置.发射出去后,子弹在屏幕中向上移动,这意
        # 味y坐标将不断减小,因此为更新子弹的位置,我们从self.y中减去self.speed_factor的值
        # 子弹发射后,其x坐标始终不变,因此子弹将沿直线垂直地往上穿行.
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)  # 函数draw.rect()
        # 使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分
