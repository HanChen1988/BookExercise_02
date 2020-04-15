# -*- coding: utf-8 -*-
# @Time : 2020/4/14 8:38 AM
# @Author : hanchen
# @File : printing_models.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 首先创建一个列表,其中包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # 模拟打印每个设计,直到没有未打印的设计为止
# #   打印每个设计后,都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#
#     # 模拟根据设计制作3D打印模型的过程
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# 定义函数print_models(),它包含两个形参:一个需要打印的设计列表和一个打印好的模型列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计,直到没有未打印的设计为止
    打印每个设计后,都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


# 定义函数show_completed_models,它包含一个形参:打印好的模型列表
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 每个函数都应只负责一项具体的工作
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# ------------------ example02 ------------------
