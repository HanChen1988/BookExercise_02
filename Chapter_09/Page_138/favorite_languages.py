# -*- coding: utf-8 -*-
# @Time : 2020/4/29 8:21 AM
# @Author : hanchen
# @File : favorite_languages.py
# @Software: PyCharm


# ------------------ example01 ------------------
from collections import OrderedDict

# 调用OrderedDict()来创建一个空的有序字典,并将其存储在favorite_languages中
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
# ------------------ example01 ------------------
