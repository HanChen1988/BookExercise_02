# -*- coding: utf-8 -*-
# @Time : 2020/4/1 8:50 上午
# @Author : hanchen
# @File : magicians.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 遍历整个列表
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 遍历整个列表
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
#
# print("Thank you, everyone. That was a great magic show!")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
#     print(magician)
#         ^
# IndentationError: expected an indented block
# 解决方法:
# 1.将紧跟着for语句后面的代码行缩进
#     print(magician)
# ------------------  error01  ------------------

# print("*" * 20)

# ------------------  error02  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
#     for magician in magicians
#                             ^
# SyntaxError: invalid syntax
# 解决方法:
# 1.for语句末尾添加冒号(:)
#     for magician in magicians:
# ------------------  error02  ------------------
