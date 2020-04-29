# -*- coding: utf-8 -*-
# @Time : 2020/4/24 8:23 AM
# @Author : hanchen
# @File : electric_car.py
# @Software: PyCharm


# ------------------ example01 ------------------
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         super().__init__(make, model, year)
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """
#         电动汽车的独特之处
#         初始化父类的属性,再初始化电动汽车特有的属性
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#     """一次模拟电动汽车电瓶的简单尝试"""
#
#     # 形参battery_size是可选的,如果没有给它提供值,电瓶容量将被设置为70.
#     def __init__(self, battery_size=70):
#         """初始化电瓶的属性"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """打印一条消息,指出电瓶的续航里程"""
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
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """
#         初始化父类的属性,再初始化电动汽车特有的属性
#         """
#         super().__init__(make, model, year)
#         # 将实例用作属性
#         self.battery = Battery()
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
"""一组可用于表示电动汽车的类"""

from car import Car


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    # 形参battery_size是可选的,如果没有给它提供值,电瓶容量将被设置为70.
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息,指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        # 将实例用作属性
        self.battery = Battery()
# ------------------ example04 ------------------
