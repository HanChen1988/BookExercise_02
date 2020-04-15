# -*- coding: utf-8 -*-
# @Time : 2020/4/14 9:35 AM
# @Author : hanchen
# @File : pizza.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 传递任意数量的实参
# # 形参名*toppings中的星号让Python创建一个名为toppings的空元组,并将收到的所有值都封装到
# #   这个元组中
# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 传递任意数量的实参
# def make_pizza(*toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with following toppings:")
    for topping in toppings:
        print("- " + topping)
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# ------------------ example03 ------------------
