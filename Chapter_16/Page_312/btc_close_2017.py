import json
import pygal

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
# 创建5个列表,分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 打印每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    # Python不能直接将包含小数点的字符串转换为整数
    # 报错信息:
    # ValueError: invalid literal for int() with base 10: '6928.6492'
    # 解决方案:
    # 首先用函数float()将字符串转换为小数,然后再用函数int()去掉小数部分(截尾取整),
    # 返回整数部分.

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# x_label_rotation=20让x轴上的日期标签顺时针旋转20°,show_minor_x_labels=False则告诉
# 图形不用显示所有的x轴标签.
line_chart.title = '收盘价(￥)'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]  # 配置x_labels_major属性,让x轴坐标每隔20天
# 显示一次,这样x轴就不会显得非常拥挤.
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图(￥).svg')
# 报错信息:
# Traceback (most recent call last):
#   File "/Users/hanchen/PycharmProjects/BookExercise_02/Chapter_16/
#   Page_312/btc_close_2017.py", line 37, in <module>
#     line_chart.render_to_file('收盘价折线图(￥)'.svg)
# AttributeError: 'str' object has no attribute 'svg'
# 解决方案:
# line_chart.render_to_file('收盘价折线图(￥).svg')
