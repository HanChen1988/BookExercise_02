# -*- coding: utf-8 -*-
# @Time : 2020/4/20 10:17 PM
# @Author : hanchen
# @File : car.py
# @Software: PyCharm


# ------------------ example01 ------------------
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 修改属性的值
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# # 直接修改属性的值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# # 修改属性的值
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# # 通过方法修改属性的值
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# # 修改属性的值
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading += miles
#
#
# my_new_car = Car('subaru', 'outback', 2013)
# print(my_new_car.get_descriptive_name())
#
# # 通过方法修改属性的值
# my_new_car.update_odometer(23500)
# my_new_car.read_odometer()
#
# # 通过方法对属性的值进行递增
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# """一个可用于表示汽车的类"""
#
#
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading += miles
#
#
# # 在一个模块中存储多个类
# class Battery():
#     """一次模拟电动汽车电瓶的简单尝试"""
#
#     def __init__(self, battery_size=70):
#         """初始化电瓶的属性"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """打印一条描述电瓶续航里程的消息"""
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#
# class ElectricCar(Car):
#     """模拟电动汽车的独特之处"""
#     def __init__(self, make, model, year):
#         """
#         初始化父类的属性,再初始化电动汽车特有的属性
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
"""一个可用于表示汽车的类"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
# ------------------ example07 ------------------
