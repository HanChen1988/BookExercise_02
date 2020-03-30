# -*- coding: utf-8 -*-
# @Time : 2020/3/30 9:37 下午
# @Author : hanchen
# @File : birthday.py
# @Software: PyCharm

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
# --snip--
#     message = "Happy " + age + "rd Birthday!"
# TypeError: can only concatenate str (not "int") to str
# 解决方法:
# 1.调用函数str(),将非字符串值表示为字符串
#     message = "Happy " + str(age) + "rd Birthday!"
# ------------------  error01  ------------------
