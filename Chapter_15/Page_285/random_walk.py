from random import choice  # 为做出随机决策,我们将所有可能的选择都存储在一个列表中,并在每
# 次做决策时都使用choice()来决定使用哪种选择.


class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):  # 将随机漫步包含的默认点数设置为5000
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步,直到列表达到指定的长度
        while len(self.x_values) < self.num_points:  # 我们建立了一个循环,这个循环不
            # 断运行,直到漫步包含所需数量的点.

            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])  # 我们使用choice([1, -1])给x_direction
            # 选择一个值,结果要么是表示向右走的1,要么是表示向左走的-1.
            x_distance = choice([0, 1, 2, 3, 4])  # 随机地选择一个0~4之间的整数,告诉
            # Python沿指定的方向走多远(x_distance).(通过包含0,我们不仅能够沿两个轴移动,还
            # 能够沿y轴移动.)
            x_step = x_direction * x_distance  # 我们将移动方向乘以移动距离,以确定沿
            # x轴移动的距离.如果x_step为正,将向右移动,为负将向左移动,而为零将垂直移动.

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance  # 如果y_step为正,就意味着向上移动,为
            # 负就意味着向下移动,而为零意味着水平移动.

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:  # 如果x_step和y_step都为零,则意味着原地
                # 踏步,我们拒绝这样的情况,接着执行下一次循环.
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step  # 为获取漫步中下一个点的x值,我们将
            # x_step与x_values中的最后一个值相加
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
