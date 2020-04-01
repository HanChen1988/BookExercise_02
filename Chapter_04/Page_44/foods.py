# -*- coding: utf-8 -*-
# @Time : 2020/4/1 10:19 下午
# @Author : hanchen
# @File : foods.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 复制列表
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
#
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friend's favorite foods are:")
# print(friend_foods)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# 使用切片复制列表,核实两个列表不同
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
# 不使用切片复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # Python将新变量friend_foods关联到包含在my_foods中的列表,
# 因此这两个变量都指向同一个列表.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# ------------------ example03 ------------------
