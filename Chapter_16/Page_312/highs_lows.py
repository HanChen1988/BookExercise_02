import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期、最高气温和最低气温
# filename = 'sitka_weather_07-2014.csv'  # 要使用的文件的名称存储在filename中.
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:  # 我们打开这个文件,并将结果文件对象存储在f中.
    reader = csv.reader(f)  # 我们调用csv.reader(),并将前面存储的文件对象作为实参传递给
    # 它,从而创建一个与该文件相关联的阅读器(reader)对象.
    header_row = next(reader)  # 调用next()并将阅读器对象传递给它时,它将返回文件中的下一
    # 行.在前面的代码中,我们只调用了next()一次,因此得到的是文件的第一行,其中包含文件头.

    # for index, column_header in enumerate(header_row):  # 对列表调用了enumerate()
    #     # 来获取每个元素的索引及其值.
    #     print(index, column_header)

    dates, highs, lows = [], [], []  # 我们创建了两个空列表,用于存储从文件中提取的日期、
    # 最高气温和最低气温.
    for row in reader:  # 遍历文件中余下的各行.阅读器对象从其停留的地方继续往下读取csv文件,
        # 每次都自动返回当前所处位置的下一行.由于我们已经读取了文件头行,这个循环从第二行开始——
        # 从这行开始包含的是实际数据.
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')  # 导入模块datetime
        # 中的datetime类,然后调用方法strptime(),并将包含所需日期的字符串作为第一个实参.
        # 第二个实参告诉Python如何设置日期的格式.在这个示例中,'%Y-'让Python将字符串中第一个
        # 连字符前面的部分视为四位的年份;'%m-'让Python将第二个连字符前面的部分视为表示月份
        # 的数字;而'%d'让Python将字符串的最后一部分视为月份中的一天(1~31).
            high = int(row[1])  # 将表示气温的字符串转换成了数字
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)  # 每次执行该循环时,我们都将索引1处(第2列)的数据附加到
            # highs末尾.
            lows.append(low)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)  # 将日期和最高气温列表传给plot(),
    # 并传递c='red'以便将数据点绘制为红色.
    plt.plot(dates, lows, c='blue', alpha=0.5)  # 使用蓝色绘制最低气温.
    # 实参alpha指定颜色的透明度.Alpha值为0表示完全透明,1(默认设置)表示完全不透明.通过将
    # alpha设置为0.5,可让红色和蓝色折现的颜色看起来更浅.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # 我们向fill_between()传递了一个x值系列:列表dates,还传递了两个y值系列:highs和lows.
    # 实参facecolor指定了填充区域的颜色.我们还将alpha设置成了较小的值0.1,让填充区域将两个
    # 数据系列连接起来的同时不分散观察者的注意力.

    # 设置图形的格式
    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    # plt.title("Daily high and low temperatures - 2014", fontsize=24)
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 我们调用了fig.autofmt_xdate()来绘制斜的日期标签,
    # 以免它们彼此重叠.
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
