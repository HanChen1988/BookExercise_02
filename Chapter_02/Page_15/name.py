# -*- coding: utf-8 -*-
# @Time : 2020/3/30 8:22 上午
# @Author : hanchen
# @File : name.py
# @Software: PyCharm

# ------------------ example01 ------------------
# # 使用方法修改字符串的大小写
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 合并(拼接)字符串
# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
#
# print(full_name)
# print("Hello, " + full_name.title() + "!")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 合并(拼接)字符串
# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
#
# message = "Hello, " + full_name.title() + "!"
# print(message)
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# # 使用制表符或换行符来添加空白
# print("Python")
# print("\tPython")
# print("Languages:\nPython\nC\nJavaScript")
# print("Languages:\n\tPython\n\tC\n\tJavaScript")
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# # 删除末尾空白
# favorite_language = 'python '
# print("'" + favorite_language + "'")
# print("'" + favorite_language.rstrip() + "'")
# print("'" + favorite_language + "'")
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# # 永久删除空白
# favorite_language = 'python '
# favorite_language = favorite_language.rstrip()
# print("'" + favorite_language + "'")
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# 删除空白
favorite_language = ' python '
print("'" + favorite_language.rstrip() + "'")  # 删除末尾空白
print("'" + favorite_language.lstrip() + "'")  # 删除开头空白
print("'" + favorite_language.strip() + "'")   # 删除两端空白
# ------------------ example07 ------------------

# print("*" * 20)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
# 解决方法:
# 1.
# 2.
# --snip--
# ------------------  error01  ------------------
