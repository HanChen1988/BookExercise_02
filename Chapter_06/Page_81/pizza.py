# -*- coding: utf-8 -*-
# @Time : 2020/4/6 1:05 下午
# @Author : hanchen
# @File : pizza.py
# @Software: PyCharm


# ------------------ example01 ------------------
# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
# ------------------ example01 ------------------
