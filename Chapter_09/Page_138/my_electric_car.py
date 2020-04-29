# -*- coding: utf-8 -*-
# @Time : 2020/4/27 11:15 PM
# @Author : hanchen
# @File : my_electric_car.py
# @Software: PyCharm


# ------------------ example01 ------------------
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# ------------------ example01 ------------------
