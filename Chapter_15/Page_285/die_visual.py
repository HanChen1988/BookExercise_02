import pygal

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子,并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)  # 我们遍历可能的点数(这里为1~6),计算每种点数在
    # results中出现了多少次.
    frequencies.append(frequency)

# 对结果进行可视化
# 条形图
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']  # 将掷D6骰子的可能结果用作x轴的标签.
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)  # 我们使用add()将一系列值添加到图表中(向它传递要给添加的值
# 指定的标签,还有一个列表,其中包含将出现在图表中的值)
hist.render_to_file('die_visual.svg')  # 我们将这个图表渲染为一个SVG文件,这种文件的扩
# 展名必须为.svg.
