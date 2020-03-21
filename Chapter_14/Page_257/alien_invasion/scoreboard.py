import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备包含最高得分和当前得分的图像
        self.prep_score()  # 将要显示的文本转换为图像,我们调用了prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))  # 函数round()通常让小数
        # 精确到小数点后多少位,其中小数位数是由第二个实参指定的.然而,如果将第二个实参指定为
        # 负数,round将圆整到最近的10、100、1000等整数倍.
        # -1让Python将stats.score的值圆整到最近的10的整数倍,并将结果存储到rounded_score
        # 中.
        # 注意:在Python2.7中,round()总是返回一个小数值,因此我们使用int()来确保报告的得分为
        # 整数.如果你使用的是Python3,可省略对int()的调用.
        score_str = "{:,}".format(rounded_score)  # 使用了一个字符串格式设置指令,它让
        # Python将数值转换为字符串时在其中插入逗号.
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 让其右边缘与屏幕右
        # 边缘相距20像素
        self.score_rect.top = 20  # 让其上边缘与屏幕上边缘也相距20像素

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))  # 我们将最高得分圆整到
        # 最近的10的整数倍
        high_score_str = "{:,}".format(high_score)  # 添加了用逗号表示的千分位分隔符
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top  # 将其top属性设置为当前得分
        # 图像的top属性

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color,
                                            self.ai_settings.bg_color)  # 根据存
        # 储在stats.level中的值创建一副图像

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right  # 其right属性设置为得分的
        # right属性
        self.level_rect.top = self.score_rect.bottom + 10  # 将top属性设置为比得分
        # 图像的bottom属性大10像素,以便在得分和等级之间留出一定的空间.

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()  # 方法prep_ships()创建一个空编组self.ships,用于存储飞船
        # 实例
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width  # 设置其x坐标,让整个
            # 飞船编组都位于屏幕左边,且每艘飞船的左边距都为10像素.
            ship.rect.y = 10  # 将y坐标设置为离屏幕上边缘10像素,让所有飞船都与得分图像对
            # 齐
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分和等级"""
        self.screen.blit(self.score_image, self.score_rect)  # 这个方法将得分图像
        # 显示到屏幕上,并将其放在score_rect指定的位置
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)  # 为在屏幕上显示飞船,我们对编组调用了draw().
        # Pygame将绘制每艘飞船.
