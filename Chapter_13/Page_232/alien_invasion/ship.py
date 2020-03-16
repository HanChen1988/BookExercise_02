import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始化位置"""
        self.screen = screen
        self.ai_settings = ai_settings  # 我们在__init__()的形参列表中添加了
        # ai_settings,让飞船能够获取其速度设置。我们将形参ai_settings的值存储在一个属性中,
        # 以便能够在update()中使用它

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  # 为加载图像，这个函数

        # 返回一个表示飞船的surface
        self.rect = self.image.get_rect()   # 获取相应surface的属性rect
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        # self.rect.center = self.screen_rect.center  # 12-2 游戏角色 练习使用
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)  # 可以使用小数来设置rect的属性,但rect
        # 将只存储这个值得整数部分，为准确地存储飞船的位置,我们定义了一个可存储小数值的新属性
        # self.center

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor  # 现在在update()中
            # 调整飞船的位置时,将self.center的值增加或减去ai_settings.ship_speed_factor
            # 的值
        if self.moving_left and self.rect.left > 0:  # 我们添加if代码块而不是
            # elif代码块，这样如果玩家同时按下左右箭头键，将先增大飞船的rect.centerx值
            # ,再降低这个值，即飞船的位置保持不变。
            # 如果使用一个elif代码块来处理向左移动的情况，右箭头键将始终处于优先地位。从向左
            # 移动切换到向右移动时，玩家可能同时按住左右箭头键，在这种情况下，前面的做法让移动
            # 更准确。
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center  # self.rect.centerx将只存储self.center的
        # 整数部分,但对显示飞船而言,这个问题不大。

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 根据self.rect指定的位置将图像
        # 绘制到屏幕上。

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
