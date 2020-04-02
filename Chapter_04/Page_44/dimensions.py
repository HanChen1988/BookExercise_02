# -*- coding: utf-8 -*-
# @Time : 2020/4/2 7:59 上午
# @Author : hanchen
# @File : dimensions.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 创建一个大小不变的矩形,将其长度和宽度存储在一个元组中
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 创建一个大小不变的矩形,将其长度和宽度存储在一个元组中
# dimensions = (200, 50)
# dimensions[0] = 250
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 创建一个大小不变的矩形,将其长度和宽度存储在一个元组中
# dimensions = (200, 50)
# # 使用for循环来遍历元组中的所有值
# for dimension in dimensions:
#     print(dimension)
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# 创建一个大小不变的矩形,将其长度和宽度存储在一个元组中
dimensions = (200, 50)
print("Original dimensions:")
# 使用for循环来遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
#     dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment
# 解决方法:
# 1.Python指出不能给元组的元素赋值
# ------------------  error01  ------------------
