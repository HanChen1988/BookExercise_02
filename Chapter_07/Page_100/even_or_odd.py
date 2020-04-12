# -*- coding: utf-8 -*-
# @Time : 2020/4/12 3:20 下午
# @Author : hanchen
# @File : even_or_odd.py
# @Software: PyCharm


# ------------------ example01 ------------------
# 判断一个数是奇数还是偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:  # 求模运算符(%),它将两个数相除并返回余数
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
# ------------------ example01 ------------------
