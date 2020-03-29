# -*- coding: utf-8 -*-
# @Time : 2020/3/29 5:34 下午
# @Author : hanchen
# @File : bar_descriptions.py
# @Software: PyCharm

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 46179, 'label': 'Description of httpie.'},
    {'value': 48138, 'label': 'Description of django.'},
    {'value': 49624, 'label': 'Description of flask.'},
]  # 定义了一个名为plot_dicts的列表,其中包含三个字典,分别针对项目HTTPPie、
# Django和Flask.每个字典都包含两个键:'value'和'label'.
# Pygal根据与键'value'相关联的数字来确定条形的高度,并使用与'label'相关联的字符串给条形
# 创建工具提示.

chart.add('', plot_dicts)  # 方法add()接受一个字符串和一个列表.这里调用add()时,
# 我们传入了一个由表示条形的字典组成的列表.
chart.render_to_file('bar_descriptions.svg')
