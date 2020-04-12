# -*- coding: utf-8 -*-
# @Time : 2020/4/12 2:39 下午
# @Author : hanchen
# @File : parrot.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 让用户输入一些文本,再将这些文本呈现给用户
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 让用户选择何时退出
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# 让用户选择何时退出
# 使用标识
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# ------------------ example03 ------------------
