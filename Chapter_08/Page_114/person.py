# -*- coding: utf-8 -*-
# @Time : 2020/4/14 8:13 AM
# @Author : hanchen
# @File : person.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 返回字典
# def build_person(first_name, last_name):
#     """返回一个字典,其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     return person
#
#
# musician = build_person('jimi', 'hendrix')
# print(musician)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# 返回字典
# 新增一个可选形参age
def build_person(first_name, last_name, age=''):
    """返回一个字典,其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
# ------------------ example02 ------------------
