# -*- coding: utf-8 -*-
# @Time : 2020/4/5 10:36 上午
# @Author : hanchen
# @File : amusement_park.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 根据年龄段收费的游乐场:
# #     4岁以下免费;
# #     4~18岁收费5美元;
# #     18岁(含)以上收费10美元.
#
# # 写法一:
# age = 12
#
# # 使用if-elif-else结构
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")
#
# # 写法二:
# age = 12
#
# # 使用if-elif-else结构
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
#
# print("Your admission cost is $" + str(price) + ".")
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 根据年龄段收费的游乐场:
# #     4岁以下免费;
# #     4~18岁收费5美元;
# #     18岁(含)以上收费10美元;
# #     65岁(含)以上收费5美元.
#
# age = 12
#
# # 使用多个elif代码块
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5
#
# print("Your admission cost is $" + str(price) + ".")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# 根据年龄段收费的游乐场:
#     4岁以下免费;
#     4~18岁收费5美元;
#     18岁(含)以上收费10美元;
#     65岁(含)以上收费5美元.

age = 12

# 省略else代码块
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
# ------------------ example03 ------------------
