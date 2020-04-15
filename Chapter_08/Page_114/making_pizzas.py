# -*- coding: utf-8 -*-
# @Time : 2020/4/15 8:56 AM
# @Author : hanchen
# @File : making_pizzas.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 导入整个模块
# # 语法:
# # import module_name
# # module_name.function_name()
# import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 导入特定的函数
# # 语法:
# # from module_name import function_name
# # from module_name import function_0, function_1, function_2  # 用逗号分隔函数名
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 使用as给函数指定别名
# #   如果要导入的函数的名称可能与程序中现有的名称冲突,或者函数的名称太长,可指定简短而独一无二
# #   别名
# # 语法:
# # from module_name import function_name as fn
# from pizza import make_pizza as mp
#
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# # 使用as给模块指定别名
# # 语法:
# # import module_name as mn
# import pizza as p
#
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# 导入模块中的所有函数
#   使用星号(*)运算符可让Python导入模块中的所有函数
# 语法:
# from module_name import *
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# ------------------ example05 ------------------

# print("*" * 20)
