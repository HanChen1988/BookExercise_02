# -*- coding: utf-8 -*-
# @Time : 2020/4/14 8:32 AM
# @Author : hanchen
# @File : greet_users.py
# @Software: PyCharm


# ------------------ example01 ------------------
# 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# ------------------ example01 ------------------
