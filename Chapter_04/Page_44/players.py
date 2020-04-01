# -*- coding: utf-8 -*-
# @Time : 2020/4/1 9:59 下午
# @Author : hanchen
# @File : players.py
# @Software: PyCharm


# ------------------ example01 ------------------
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
#
# # 输出列表中前三个元素
# print(players[0:3], "\n")
#
# # 提取列表的第2~4个元素
# print(players[1:4], "\n")
#
# # 没有指定第一个索引,Python将自动从列表开头开始
# print(players[:4], "\n")
#
# # 没有指定第二个索引,Python将自动终止于列表末尾
# print(players[2:], "\n")
#
# # 输出列表最后三个元素
# print(players[-3:], "\n")
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# ------------------ example02 ------------------
