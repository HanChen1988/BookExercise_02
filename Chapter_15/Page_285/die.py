from random import randint


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):  # 如果没有指定任何实参,面数默认为6.如果指定了实参,
        # 这个值将用于设置骰子的面数.
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.num_sides)  # 返回一个1和面数之间的随机数.这个函数可能
        # 返回起始值1、终止值num_sides或这两个值之间的任何整数.
