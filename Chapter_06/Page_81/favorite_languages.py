# -*- coding: utf-8 -*-
# @Time : 2020/4/6 10:32 上午
# @Author : hanchen
# @File : favorite_languages.py
# @Software: PyCharm


# ------------------ example01 ------------------
# # 由类似对象组成的字典
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# # 使用拼接运算符(+)
# print("Sarah's favorite language is " +
#       favorite_languages['sarah'].title() +
#       ".")
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# # 遍历所有的键-值对
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# # 遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# # 遍历字典时,会默认遍历所有的键
# for name in favorite_languages.keys():
#     print(name.title())
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# # 遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("  Hi " + name.title() +
#               ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# # 遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# # 方法keys()并非只能用于遍历;实际上,它返回一个列表,其中包含字典中的所有键.
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# # 按顺序遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# # 使用函数sorted()来获得按特定顺序排列的键列表的副本
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# # 遍历字典中的所有值
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# print("The following languages have been mentioned:")
# # 使用方法values(),它返回一个值列表
# for language in favorite_languages.values():
#     print(language.title())
# ------------------ example07 ------------------

# print("*" * 20)

# ------------------ example08 ------------------
# # 遍历字典中的所有值
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# print("The following languages have been mentioned:")
# # 为剔除重复项,可使用集合(set).
# for language in set(favorite_languages.values()):
#     print(language.title())
# ------------------ example08 ------------------

# print("*" * 20)

# ------------------ example09 ------------------
# # 在字典中存储列表
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
# }
#
# for name, languages in favorite_languages.items():
#     print("\n" + name.title() + "'s favorite languages are:")
#     for language in languages:
#         print("\t" + language.title())
# ------------------ example09 ------------------

# print("*" * 20)

# ------------------ example10 ------------------
# 在字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " +
              languages[0].title() + ".")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
# ------------------ example10 ------------------
