# -*- coding: utf-8 -*-
# @Time : 2020/4/28 8:00 AM
# @Author : hanchen
# @File : my_cars.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 从一个模块中导入多个类,用逗号分隔各个类
# from car import Car, ElectricCar
# # 创建了一辆大众甲壳虫普通汽车
# my_beetle = Car('volkwagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
# # 创建了一辆特斯拉Roadster电动汽车
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 导入整个模块,使用句点表示法访问需要的类
# import car
#
# my_beetle = car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# ------------------ example03 ------------------
