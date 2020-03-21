import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 折线图
plt.plot(input_values, squares, linewidth=5)  # 参数linewidth决定了plot()绘制的线条
# 的粗细.

# 设置图表标题,并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)  # 函数title()给图表指定标题.参数fontsize
# 指定了图表中文字的大小.
plt.xlabel("Value", fontsize=14)  # 每条轴设置标题.
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)  # 指定的实参将影响x轴和y轴上的刻度(
# axis='both'),并将刻度标记的字号设置为14.

plt.show()
