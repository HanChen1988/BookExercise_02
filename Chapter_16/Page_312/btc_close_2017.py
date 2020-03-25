import json
import pygal
import math
from itertools import groupby

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

# 封装成函数前的绘制代码

# 1.收盘价折线图(￥).svg
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# # x_label_rotation=20让x轴上的日期标签顺时针旋转20°,show_minor_x_labels=False则
# # 告诉图形不用显示所有的x轴标签.
# line_chart.title = '收盘价(￥)'
# line_chart.x_labels = dates
# N = 20  # x轴坐标每隔20天显示一次
# line_chart.x_labels_major = dates[::N]  # 配置x_labels_major属性,让x轴坐标
# # 每隔20天显示一次,这样x轴就不会显得非常拥挤.
# line_chart.add('收盘价', close)
# line_chart.render_to_file('收盘价折线图(￥).svg')
# 报错信息:
# Traceback (most recent call last):
#   File "/Users/hanchen/PycharmProjects/BookExercise_02/Chapter_16/
#   Page_312/btc_close_2017.py", line 37, in <module>
#     line_chart.render_to_file('收盘价折线图(￥)'.svg)
# AttributeError: 'str' object has no attribute 'svg'
# 解决方案:
# line_chart.render_to_file('收盘价折线图(￥).svg')

# 2.收盘价对数变换折线图(￥).svg
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# # x_label_rotation=20让x轴上的日期标签顺时针旋转20°,show_minor_x_labels=False则
# # 告诉图形不用显示所有的x轴标签.
# line_chart.title = '收盘价对数变换(￥)'
# line_chart.x_labels = dates
# N = 20  # x轴坐标每隔20天显示一次
# line_chart.x_labels_major = dates[::N]  # 配置x_labels_major属性,让x轴坐标
# # 每隔20天显示一次,这样x轴就不会显得非常拥挤.
# close_log = [math.log10(_) for _ in close]
# line_chart.add('收盘价', close_log)
# line_chart.render_to_file('收盘价对数变换折线图(￥).svg')


# 封装成函数后的绘制代码
def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        # 将x轴与y轴的数据合并、排序,再用函数groupby分组.
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 分组之后,求出每组的均值,存
        # 储到xy_map变量中.
    x_unique, y_mean = [*zip(*xy_map)]  # 将xy_map中存储的x轴与y轴数据分离
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    # line_chart.render_to_file(title+'.svg')
    return line_chart


# 绘制2017年1月到11月的月日均值
idx_month = dates.index('2017-12-01')  # 通过dates查找2017-12-01的索引位置,确定
# 月份和收盘价的取值范围.
line_chart_month = draw_line(months[:idx_month], close[:idx_month],
                             '收盘价月日均值(￥)', '月日均值')
line_chart_month.render_to_file(line_chart_month.title+'.svg')

# 绘制前49周(2017-01-02~2017-12-10)的周日均值
idx_week = dates.index('2017-12-11')  # 通过dates查找2017-12-11的索引位置,确定
# 周数和收盘价的取数范围.2017年1月1日是周日,归属为2016年第52周,因此取数时需要将第一天去掉.
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week],
                            '收盘价周日均值(￥)', '周日均值')
line_chart_week.render_to_file(line_chart_week.title+'.svg')

# 绘制前49周(2017-01-02~2017-12-10)的星期均值
idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
      'Sunday']  # 我们列出一周七天的英文单词
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]  # 将weekdays的内
# 容替换成1~7的整数
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week],
                               '收盘价星期均值(￥)', '星期均值')  # 函数draw_line在
# 处理数据时按周几的顺序排列,就会将周一放在列表的第一位,周日放在列表的第七位.
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六',
                               '周日']  # 将图形的x轴标签替换为中文.
line_chart_weekday.render_to_file(line_chart_weekday.title+'.svg')

# 创建一个名为收盘价Dashboard.html的网页文件,然后将每幅图都添加到页面中.
with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta \
                    charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图(￥).svg', '收盘价对数变换折线图(￥).svg', '收盘价月日均值(￥).svg',
        '收盘价周日均值(￥).svg', '收盘价星期均值(￥).svg'
    ]:
        html_file.write('<object type="image/svg+xml" data="{0}" height=500> \
                        </object>\n'.format(svg))  # 设置svg图形的默认高度为500像素.
    html_file.write('</body></html>')
