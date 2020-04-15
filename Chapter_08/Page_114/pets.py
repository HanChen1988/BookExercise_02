# -*- coding: utf-8 -*-
# @Time : 2020/4/13 8:53 AM
# @Author : hanchen
# @File : pets.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 位置实参
# # 显示宠物信息的函数
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# # 函数调用中实参的顺序要与函数定义中形参的顺序一致
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 关键字实参(传递给函数的名称-值对)
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 默认值
# # 使用默认值时,在形参列表中必须先列出没有默认值的形参,再列出有默认值的形参.
# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# # 一条名为Willie的小狗
# describe_pet(pet_name='willie')
# describe_pet('willie')
# # 一只名为Harry的仓鼠
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# 避免实参错误
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
# ------------------ example04 ------------------
