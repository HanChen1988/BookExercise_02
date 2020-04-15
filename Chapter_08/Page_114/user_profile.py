# -*- coding: utf-8 -*-
# @Time : 2020/4/15 8:38 AM
# @Author : hanchen
# @File : user_profile.py
# @Software: PyCharm


# ------------------ example01 ------------------
# 创建用户的简介
# 形参**user_info中的两个星号让Python创建一个名为user_info的空字典,并将收到的
#   所有名称-值对都封装到这个字典中
def build_profile(first, last, **user_info):
    """创建一个字典,其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
# ------------------ example01 ------------------
