# -*- coding: utf-8 -*-
# @Time : 2020/4/13 8:36 AM
# @Author : hanchen
# @File : greeter.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 定义函数
# # 关键字def告诉Python你要定义一个函数
# def greet_user():
#     """显示简单的问候语"""  # 被称为文档字符串的注释
#     print("Hello!")
#
#
# greet_user()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 向函数传递信息
# # 在函数定义def greet_user()的括号内添加username,可让函数接受你给username指定的任何值.
# def greet_user(username):  # 变量username是一个形参,函数完成其工作所需的一项信息
#     """显示简单的问候语"""
#     print("Hello, " + username.title() + "!")
#
#
# # 值jesse是一个实参.实参是调用函数时传递给函数的信息.
# greet_user('jesse')
# greet_user('sarah')
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
# ------------------ example03 ------------------
