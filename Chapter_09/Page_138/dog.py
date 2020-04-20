# -*- coding: utf-8 -*-
# @Time : 2020/4/20 9:25 PM
# @Author : hanchen
# @File : dog.py
# @Software: PyCharm


# ------------------ example01 ------------------
class Dog():
    """一次模拟小狗的简单尝试"""

    # 类中的函数称为方法
    # __init__()是一个特殊的方法,每当类创建新实例时,Python都会自动运行它
    #   这个方法的名称中,开头和末尾各有两个下划线,这是一种约定,旨在避免Python默认方法
    #   与普通方法发生名称冲突.
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name  # 获取存储在形参name中的值,并将其存储到变量name中,
        # 然后该变量被关联到当前创建的实例.
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 根据类创建实例
# # 访问属性
#
#
# my_dog = Dog('whilie', 6)
#
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 根据类创建实例
# # 调用方法
#
#
# my_dog = Dog('whilie', 6)
# my_dog.sit()
# my_dog.roll_over()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# 根据类创建实例
# 创建多个实例


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
#     print("\nYour dog's name is " + your_dog.title() + ".")
# AttributeError: 'Dog' object has no attribute 'title'
# 解决方法:
# 1.添加类的属性name
#     print("\nYour dog's name is " + your_dog.name.title() + ".")
# ------------------  error01  ------------------
