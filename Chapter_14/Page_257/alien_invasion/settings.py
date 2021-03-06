class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200  # 在pygame中，原点(0, 0)位于屏幕左上角,向右下方移动
        # 时,坐标值将增大
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 创建了一种背景色，并将其存储在bg_color中
        # ,浅灰色
        # self.bg_color = (0, 0, 255)  # 12-1 蓝色天空 练习使用
        # 在Pygame中，颜色是以RGB值指定的，这种颜色由红色、绿色和蓝色值组成
        # ,其中每个值的可能取值范围都是0~255。颜色值(255,0,0)表示红色,(0,255,0)表示绿色
        # ,而(0,0,255)表示蓝色

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # 这将未消失的子弹数限制为3颗

        # 外星人设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1  # 设置为1.1能够将游戏节奏提高到够快,让游戏既有难度,又
        # 并非不可完成.
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5  # 设置飞船的初始速度
        self.bullet_speed_factor = 3  # 设置子弹的初始速度
        self.alien_speed_factor = 1  # 设置外星人的初始速度

        # fleet_direction为1表示向右移,为-1表示向左移
        self.fleet_direction = 1  # 我们使用值1和-1来表示它们,并在外星人群改变方向时在这
        # 两个值之间切换.另外,鉴于向右移动时需要增大每个外星人的x坐标,而向左移动时需要减小每个
        # 外星人的x坐标,使用数字来表示方向更合理.

        # 记分
        self.alien_points = 50  # 为确保每次开始新游戏时这个值都会被重置,我们在
        # initialize_dynamic_settings()中设置它.

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)  # 确定点数在不断增加后,一定要删除这条print语句,否则
        # 它可能会影响游戏的性能以及分散玩家的注意力.
