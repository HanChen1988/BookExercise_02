# -*- coding: utf-8 -*-
# @Time : 2020/4/5 9:44 上午
# @Author : hanchen
# @File : toppings.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 检查是否不相等
# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 顾客点的配料
# requested_toppings = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     print("Adding " + requested_topping + ".")
#
# print("\nFinished making your pizza!")
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     # 检查顾客点的是否是青椒
#     if requested_topping == 'green peppers':
#         # 指出不能点青椒的原因
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")
#
# print("\nFinished making your pizza!")
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# # 确定列表是不是空的
# requested_toppings = []
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# print("*" * 20)

# ------------------ example06 ------------------
# 使用多个列表
# 第一个列表包含比萨店供应的配料
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
# 第二个列表包含顾客点的配料
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
# ------------------ example06 ------------------

# print("*" * 20)
