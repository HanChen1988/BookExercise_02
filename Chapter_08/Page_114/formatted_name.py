# -*- coding: utf-8 -*-
# @Time : 2020/4/13 9:33 AM
# @Author : hanchen
# @File : formatted_name.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 返回值
# # 返回简单值
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 让实参变成可选的
# def get_formatted_name(first_name, middle_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:  # Python将非空字符串解读为True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
# ------------------ example03 ------------------
