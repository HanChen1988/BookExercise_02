# -*- coding: utf-8 -*-
# @Time : 2020/3/30 11:34 下午
# @Author : hanchen
# @File : bicycles.py
# @Software: PyCharm

# ------------------ example01 ------------------
# # 将列表打印出来
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 访问列表元素
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])  # 当你请求获取列表元素时,Python只返回该元素,而不包括方括号和引号.
# print(bicycles[0].title())
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 访问索引1和3处的自行车:
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[1])
# print(bicycles[3])
# # 访问最后一个列表元素:
# print(bicycles[-1])
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# 从列表中提取第一款自行车,并使用这个值来创建一条消息
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
# ------------------ example04 ------------------
