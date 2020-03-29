# -*- coding: utf-8 -*-
# @Time : 2020/3/29 5:36 下午
# @Author : hanchen
# @File : python_repos.py
# @Software: PyCharm

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 增加重试连接次数
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
# 关闭多余的连接
s.keep_alive = False

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = s.get(url)  # 调用get()并将URL传递给它,再将响应对象存储在变量r中.
print("Status code:", r.status_code)  # 响应对象包含一个名为status_code的属性,它让
# 我们知道请求是否成功了(状态码200表示请求成功).打印status_code,核实调用是否成功了.

# 将API响应存储在一个变量中
response_dict = r.json()  # 这个API返回JSON格式的信息,因此我们使用方法json()将这些信息
# 转换为一个Python字典.将转换得到的字典存储在response_dict中.
print("Total repositories:", response_dict['total_count'])  # 我们打印了与
# 'total_count'相关联的值,它指出了GitHub总共包含多少个Python仓库.

# 探索有关仓库的信息
repo_dicts = response_dict['items']  # 与'item'相关联的值是一个列表,其中包含很多字典,
# 而每个字典都包含有关一个Python仓库的信息.我们将这个字典列表存储在repo_dicts中.
print("Repositories returned:", len(repo_dicts))  # 我们打印repo_dicts的长度,以
# 获悉我们获得了多少个仓库的信息.

# 研究第一个仓库
# repo_dict = repo_dicts[0]  # 为更深入地了解返回的有关每个仓库的信息,我们提取了
# repo_dicts中的第一个字典,并将其存储在repo_dict中.
# print("\nKeys:", len(repo_dict))  # 我们打印这个字典包含的键数,看看其中有多少信息.
# for key in sorted(repo_dict.keys()):
#     print(key)  # 我们打印这个字典的所有键,看看其中包含哪些信息.

# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print('Name:', repo_dict['name'])  # 打印项目的名称
#     print('Owner:', repo_dict['owner']['login'])  # 项目所有者是用一个字典表示的.
#     # 我们使用键owner来访问表示所有者的字典,再使用键key来获取所有者的登录名.
#     print('Stars:', repo_dict['stargazers_count'])  # 打印项目获得了多少个星的评级
#     print('Repository:', repo_dict['html_url'])  # 项目在GitHub仓库的URL
#     print('Created:', repo_dict['created_at'])  # 显示项目的创建时间
#     print('Updated:', repo_dict['updated_at'])  # 最后一次更新的时间
#     print('Description:', repo_dict['description'])  # 打印仓库的描述

names, plot_dicts = [], []  # 创建两个空列表,用于存储将包含在图表中的信息.我们需要
# 每个项目的名称,用于给条形加上标签.
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])  # 在循环中,将项目的名称附加到列表的末尾

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],  # Pygal根据与键'xlink'相关联的URL将每个
        # 条形都转换为活跃的链接.单击图表中的任何条形时,都将在浏览器中打开一个新的标签页,
        # 并在其中显示相应项目的GitHub页面.
    }  # 在循环内部,对于每个项目,我们都创建了字典plot_dict.在这个字典中,我们使用键'value'
    # 存储了星数,并使用键'label'存储了项目描述.
    plot_dicts.append(plot_dict)  # 将字典plot_dict附加到plot_dicts末尾

# 可视化
my_style = LS('#333366', base_style=LCS)  # 将其基色设置为深蓝色

my_config = pygal.Config()  # 创建一个Pygal类Config的实例,并将其命名为my_config
my_config.x_label_rotation = 45  # 让标签绕x轴顺时针旋转45度
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24  # 图表标题的字体大小
my_config.label_font_size = 24  # 副标签的字体大小.在这个图表中,副标签是x轴上的项目名
# 以及y轴上的大部分数字.
my_config.major_label_font_size = 18  # 主标签的字体大小.在这个图表中,主标签是y轴上
# 为5000整数倍的刻度.这些标签应更大,以与副标签区分开来.
my_config.truncate_label = 15  # 使用truncate_label将较长的项目名缩短为15个字符
# (如果你将鼠标指向屏幕上被截短的项目名,将显示完整的项目名).
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000  # 设置自定义宽度,让图表更充分地利用浏览器中的可用空间.

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'  # 给图表指定了标题
chart.x_labels = names  # 将属性x_labels设置为列表names

chart.add('', plot_dicts)  # 添加数据时,将标签设置成了空字符串
chart.render_to_file('python_repos.svg')

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
# urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.github.com', \
# port=443): Max retries exceeded with url: /search/repositories?q= \
# language:python&sort=stars (Caused by NewConnectionError( \
# '<urllib3.connection.VerifiedHTTPSConnection object at 0x110f05890>:  \
# Failed to establish a new connection: [Errno 61] Connection refused'))
# 解决方法:
# 1.1增加重试连接次数
#     requests.adapters.DEFAULT_RETRIES = 5
#     s = requests.session()
# 1.2关闭多余的连接
#     s.keep_alive = False
# 1.3调用get()并将URL传递给它,再将响应对象存储在变量r中.
#     r = s.get(url)
# ------------------  error01  ------------------

# ------------------  error02  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
# AttributeError: 'NoneType' object has no attribute 'decode'
# 解决方法:
# 1.直接将其改为字符串
#     # 直接将其改为字符串
#     'label': str(repo_dict['description']),
# 2.检查repo_dict['description']是否为空，若为空则填充
#     # 检查description是否为空，若为空则填充
#     description = repo_dict['description']
#     if not description:
#         description = 'No description provided.'
# ------------------  error02  ------------------
