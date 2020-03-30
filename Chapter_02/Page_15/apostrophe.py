# -*- coding: utf-8 -*-
# @Time : 2020/3/30 9:36 上午
# @Author : hanchen
# @File : apostrophe.py
# @Software: PyCharm

# 正确使用单引号和双引号

# 正确写法:
message = "One of Python's strengths is its diverse community."
print(message)

# # 错误写法:
# message = 'One of Python's Strengths is its diverse community.'
# print(message)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
# SyntaxError: invalid syntax
# 解决方法:
# 1.字符串中含撇号,使用双引号
#     message = "One of Python's strengths is its diverse community."
#     print(message)
# ------------------  error01  ------------------
