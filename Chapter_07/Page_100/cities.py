# -*- coding: utf-8 -*-
# @Time : 2020/4/12 4:29 下午
# @Author : hanchen
# @File : cities.py
# @Software: PyCharm


# ------------------ example01 ------------------
# 使用break退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
# ------------------ example01 ------------------
