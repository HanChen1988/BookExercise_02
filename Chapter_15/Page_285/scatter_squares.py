import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)  # 使用实参s设置了绘制图形时使用的点的尺寸.

# x_values = [1, 2, 3, 4, 5]  # 列表x_values包含要计算其平方值的数字.
# y_values = [1, 4, 9, 16, 25]  # 列表y_values包含前述每个数字的平方值.

x_values = list(range(1, 1001))  # 创建一个包含x值的列表,其中包含数字1~1000.
y_values = [x**2 for x in x_values]  # 一个生成y值的列表解析,它遍历x值
# (for x in x_values),计算其平方值(x**2),并将结果存储到列表y_values中.

# 散点图
# 1.使用自定义颜色-颜色名称
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)  # 要删除数据点
# 的轮廓,可在调用scatter()时传递实参edgecolor='none'.传递实参c将其设置为要使用的颜色的名称

# 2.使用自定义颜色-RGB
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)  # 可以
# 使用RGB颜色模式自定义颜色.要指定自定义颜色,可传递参数c,并将其设置为一个元组.其中包含三个0~1
# 之间的小数值,它们分别表示红色、绿色和蓝色分量.c=(0, 0, 0.8)创建一个由淡蓝色点组成的散点图.

# 3.使用颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)  # 将参数c设置成了一个y值列表,并使用参数cmap告诉
# pyplot使用那个颜色映射.这些代码将y值较小的点显示为浅蓝色,并将y值较大的点显示为深蓝色.

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)  # which一共3个参数
# ['major' ， 'minor'，'both'].默认是major表示主刻度,后面分别为次刻度及主次刻度都显示

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])  # 使用函数axis()指定了每个坐标轴的取值范围.函数axis()
# 要求提供四个值: x和y坐标轴的最小值和最大值.在这里,我们将x坐标轴的取值范围设置为0~1100,并将
# y坐标轴的取值范围设置为0~1100000.

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')  # 第一个实参指定要以什么样的文
# 件名保存图表,这个文件将存储到scatter_squares.py所在的目录中;第二个参数指定将图表多余的空
# 白区域裁剪掉.
