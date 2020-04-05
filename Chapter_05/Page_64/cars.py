# -*- coding: utf-8 -*-
# @Time : 2020/4/5 9:18 上午
# @Author : hanchen
# @File : cars.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 遍历一个汽车列表
# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())  # 全大写的方式打印
#     else:
#         print(car.title())  # 首字母大写的方式打印
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 检查是否相等
# car = 'bmw'  # 一个等号是陈述
# print(car == 'bmw', '\n')  # 两个等号是发问
#
# car = 'audi'
# print(car == 'bmw')
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# 检查是否相等时不考虑大小写
car = 'Audi'
print(car == 'audi', '\n')

car = 'Audi'
print(car.lower() == 'audi')  # 不修改存储在变量中的值
print(car)
# ------------------ example03 ------------------
