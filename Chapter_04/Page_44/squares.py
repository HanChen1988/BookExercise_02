# -*- coding: utf-8 -*-
# @Time : 2020/4/1 9:45 上午
# @Author : hanchen
# @File : squares.py
# @Software: PyCharm


# ------------------ example01 ------------------
# 将前10个整数的平方加入到一个列表中
squares = []  # 创建一个空列表
for value in range(1, 11):  # 使用函数range()让Python遍历1~10的值
    # square = value ** 2  # 计算当前值的平方,并将结果存储到变量square中
    # squares.append(square)  # 将新计算得到的平方值附加到列表squares末尾
    squares.append(value ** 2)

print(squares)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # 最大值
print(max(digits))  # 最小值
print(sum(digits))  # 总和
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
# 列表解析
squares = [value ** 2 for value in range(1, 11)]  # 定义一个表达式,用于生成你要存储
# 到列表中的值.编写一个for循环,用于给表达式提供值.
# 注意: for语句末尾没有冒号
print(squares)
# ------------------ example03 ------------------
