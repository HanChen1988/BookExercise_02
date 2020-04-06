# -*- coding: utf-8 -*-
# @Time : 2020/4/5 10:14 下午
# @Author : hanchen
# @File : alien.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 外星人的信息
# alien_0 = {'color': 'green', 'points': 5}
#
# print(alien_0['color'])
# print(alien_0['points'])
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 访问字典中的值
# alien_0 = {'color': 'green', 'points': 5}
#
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 添加键-值对
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# # Python不关心键-值对的添加顺序,而只关心键和值之间的关联关系
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# # 先创建一个空字典
# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# # 修改字典中的值
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
#
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# # 修改字典中的值
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
#
# # 向右移动外星人
# # 据外星人当前速度决定将其移动多远
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # 这个外星人的速度一定很快
#     x_increment = 3
#
# # 新位置等于老位置加上增量
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# 删除键-值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# 使用del语句将相应的键-值对彻底删除
del alien_0['points']
print(alien_0)
# ------------------ example07 ------------------
