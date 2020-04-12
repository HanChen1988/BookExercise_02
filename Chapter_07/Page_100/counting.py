# -*- coding: utf-8 -*-
# @Time : 2020/4/12 4:12 下午
# @Author : hanchen
# @File : counting.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # while循环从1数到5
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        # 执行continue语句,让Python忽略余下的代码,并返回到循环的开头
        continue

    print(current_number)
# ------------------ example02 ------------------
