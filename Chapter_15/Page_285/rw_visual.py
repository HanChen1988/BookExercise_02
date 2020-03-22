import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态,就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例,并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))  # 函数figure()用于指定图表的宽度、高度、分辨率和背景色.
    # 你需要给形参figsize指定一个元组,向matplotlib指出绘图窗口的尺寸,单位为英寸.
    # 使用形参dpi向figure()传递该分辨率,以有效地利用可用的屏幕空间.

    point_numbers = list(range(rw.num_points))  # 我们使用了range()生成了一个数字列
    # 表,其中包含的数字个数与漫步包含的点数相同.
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)  # 为修改坐标轴,使用了函数plt.axes()
    # 来将每条坐标轴的可见性都设置为False.
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
