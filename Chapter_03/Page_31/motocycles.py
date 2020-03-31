# -*- coding: utf-8 -*-
# @Time : 2020/3/31 8:33 上午
# @Author : hanchen
# @File : motocycles.py
# @Software: PyCharm

# ------------------ example01 ------------------
# # 修改列表元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# motorcycles[0] = 'ducati'
# print(motorcycles)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 在列表末尾添加元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# motorcycles.append('ducati')
# print(motorcycles)
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 在列表末尾添加元素
# motorcycles = []
#
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
#
# print(motorcycles)
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# # 在列表中插入元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
#
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# # 使用del语句删除元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# del motorcycles[0]
# print(motorcycles)
#
# print("*" * 20)
#
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# del motorcycles[1]
# print(motorcycles)
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# # 使用方法pop()删除元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
#
# print("*" * 20)
#
# motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + ".")
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# # 弹出列表中任何位置处的元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
#
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# ------------------ example07 ------------------

# print("*" * 20)

# ------------------ example08 ------------------
# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print("*" * 20)

# 根据值删除元素,打印一条消息,指出要将其从列表中删除的原因
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)  # 方法remove()只删除第一个指定的值.
# 如果要删除的值可能在列表中出现多次,就需要使用循环来判断是否删除了所有这样的值.
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
# ------------------ example08 ------------------
