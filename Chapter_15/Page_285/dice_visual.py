import pygal

from die import Die

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 掷骰子多次,并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()  # 计算每次的总点数
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # 可能出现的最大点数12为两个骰子的最大
# 可能点数之和,我们将这个值存储在了max_result中.
for value in range(2, max_result+1):
    frequency = results.count(value)  # 我们遍历可能的点数,计算每种点数在results中出现
    # 了多少次.
    frequencies.append(frequency)

# 对结果进行可视化
# 条形图
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)  # 我们使用add()将一系列值添加到图表中(向它传递要给
# 添加的值指定的标签,还有一个列表,其中包含将出现在图表中的值)
hist.render_to_file('dice_visual.svg')  # 我们将这个图表渲染为一个SVG文件,这种文件的扩
# 展名必须为.svg.
