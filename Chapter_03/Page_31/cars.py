# -*- coding: utf-8 -*-
# @Time : 2020/3/31 9:17 上午
# @Author : hanchen
# @File : cars.py
# @Software: PyCharm

# ------------------ example01 ------------------
# # 使用方法sort()对列表进行永久性排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
#
# print("*" * 20)
#
# # 按与字母顺序相反的顺序排列列表元素,向sort()方法传递参数reverse=True.
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 使用函数sorted()对列表进行临时排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
#
# print("Here is the original list:")
# print(cars)
#
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print(sorted(cars, reverse=True))  # 要按与字母顺序相反的顺序显示列表,可向函数
# # sorted()传递参数reverse=True.
#
# print("\nHere is the original list again:")
# print(cars)
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 倒着打印列表
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
#
# cars.reverse()  # 反转列表元素的排列顺序,方法reverse()永久性地修改列表元素的排列顺序.
# print(cars)
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# # 确定列表的长度
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))  # 计算列表元素数时从1开始,因此确定列表长度时,你应该不会遇到差一错误.
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# 使用列表时避免索引错误,索引是从0开始的
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[2])

print("*" * 20)

# 访问最后一个列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

# motorcycles = []
# print(motorcycles[-1])
# ------------------ example05 ------------------

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
#     print(motorcycles[3])
# IndexError: list index out of range
# 解决方法:
# 1.将列表或其长度打印出来,修改索引值
#     print(motorcycles[2])
# ------------------  error01  ------------------
