# -*- coding: utf-8 -*-
# @Time : 2020/3/29 5:01 下午
# @Author : hanchen
# @File : hu_submissions.py
# @Software: PyCharm

import requests

from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)  # 这个API调用返回一个列表
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()  # 响应文本转换为一个Python列表,并将其存储在submission_ids中
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章,都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],  # 文章的标题
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        # 讨论页面的链接
        'comments': response_dict.get('descendants', 0),  # 文章现有的评论数
        # 如果文章还没有评论,响应字典中将没有键'descendants'.不确定某个键是否包含在字典中
        # 时,可以使用方法dict.get(),它在指定的键存在时返回与之相关联的值,并在指定的键不存在
        # 时返回你指定的值(这里是0).
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)  # 根据评论数对字典列表submission_dicts
# 进行排序,为此,使用了模块operator中的函数itemgetter().向这个函数传递了键'comments',
# 它将从这个列表的每个字典中提取与键'comments'相关联的值.
# 函数sorted()将根据这种值对列表进行排序.我们将列表按降序排列,即评论最多的文章位于最前面.

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link']),
    print("Comments:", submission_dict['comments'])
