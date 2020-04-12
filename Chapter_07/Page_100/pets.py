# -*- coding: utf-8 -*-
# @Time : 2020/4/12 5:01 下午
# @Author : hanchen
# @File : pets.py
# @Software: PyCharm


# ------------------ example01 ------------------
# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
# ------------------ example01 ------------------
