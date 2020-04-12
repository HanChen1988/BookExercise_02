# -*- coding: utf-8 -*-
# @Time : 2020/4/12 2:43 下午
# @Author : hanchen
# @File : greeter.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 准确地指出你希望用户提供什么样的信息
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 准确地指出你希望用户提供什么样的信息
# # 提示超过一行,可将提示存储在一个变量中
# prompt = "If you tell us who you are, we can personalize the messages you " \
#          "see."
# # 运算符+=在存储在prompt中的字符串末尾附加一个字符串
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print("\nHello, " + name + "!")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 使用int()来获取数值输入
# age = input("How old are you? ")
# print(age)
# print(type(age))
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# 使用int()来获取数值输入
age = input("How old are you? ")
# 函数int()将数字的字符串表示转换为数值表示
age = int(age)
print(age >= 18)
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
#     print(age >= 18)
# TypeError: '>=' not supported between instances of 'str' and 'int'
# 解决方法:
# 1.将字符串转换为整数,再进行比较
#     age = int(age)
# ------------------  error01  ------------------
