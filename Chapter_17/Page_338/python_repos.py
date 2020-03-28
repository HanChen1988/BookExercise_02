import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 报错信息:
# Traceback (most recent call last):
# --snip--
# ConnectionRefusedError: [Errno 61] Connection refused
#
# Traceback (most recent call last):
# --snip--
# urllib3.exceptions.NewConnectionError: <urllib3.connection \
# .VerifiedHTTPSConnection object at 0x110f05890>: Failed to establish \
# a new connection: [Errno 61] Connection refused
#
# Traceback (most recent call last):
# --snip--
# urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.github.com', \
# port=443): Max retries exceeded with url: /search/repositories?q= \
# language:python&sort=stars (Caused by NewConnectionError( \
# '<urllib3.connection.VerifiedHTTPSConnection object at 0x110f05890>:  \
# Failed to establish a new connection: [Errno 61] Connection refused'))
#
# Traceback (most recent call last):
# --snip--
# requests.exceptions.ConnectionError: HTTPSConnectionPool( \
# host='api.github.com', port=443): Max retries exceeded with url:  \
# /search/repositories?q=language:python&sort=stars ( \
# Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection \
# object at 0x110f05890>: Failed to establish a new connection:  \
# [Errno 61] Connection refused'))
#
# 解决方法:
# 增加重试连接次数
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
# 关闭多余的连接
s.keep_alive = False

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = s.get(url)  # 调用get()并将URL传递给它,再将响应对象存储在变量r中.
print("Status code:", r.status_code)  # 响应对象包含一个名为status_code的属性,它让
# 我们知道请求是否成功了(状态码200表示请求成功).打印status_code,核实调用是否成功了.

# 将API响应存储在一个变量中
response_dict = r.json()  # 这个API返回JSON格式的信息,因此我们使用方法json()将这些信息
# 转换为一个Python字典.将转换得到的字典存储在response_dict中.
print("Total repositories:", response_dict['total_count'])  # 我们打印了与
# 'total_count'相关联的值,它指出了GitHub总共包含多少个Python仓库.

# 探索有关仓库的信息
repo_dicts = response_dict['items']  # 与'item'相关联的值是一个列表,其中包含很多字典,
# 而每个字典都包含有关一个Python仓库的信息.我们将这个字典列表存储在repo_dicts中.
# print("Repositories returned:", len(repo_dicts))  # 我们打印repo_dicts的长度,以
# 获悉我们获得了多少个仓库的信息.

# 研究第一个仓库
# repo_dict = repo_dicts[0]  # 为更深入地了解返回的有关每个仓库的信息,我们提取了repo_dicts
# 中的第一个字典,并将其存储在repo_dict中.
# print("\nKeys:", len(repo_dict))  # 我们打印这个字典包含的键数,看看其中有多少信息.
# for key in sorted(repo_dict.keys()):
#     print(key)  # 我们打印这个字典的所有键,看看其中包含哪些信息.

# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print('Name:', repo_dict['name'])  # 打印项目的名称
#     print('Owner:', repo_dict['owner']['login'])  # 项目所有者是用一个字典表示的.
#     # 我们使用键owner来访问表示所有者的字典,再使用键key来获取所有者的登录名.
#     print('Stars:', repo_dict['stargazers_count'])  # 打印项目获得了多少个星的评级
#     print('Repository:', repo_dict['html_url'])  # 项目在GitHub仓库的URL
#     print('Created:', repo_dict['created_at'])  # 显示项目的创建时间
#     print('Updated:', repo_dict['updated_at'])  # 最后一次更新的时间
#     print('Description:', repo_dict['description'])  # 打印仓库的描述

names, stars = [], []  # 创建两个空列表,用于存储将包含在图表中的信息.我们需要每个项目的
# 名称,用于给条形加上标签,我们还需要知道项目获得了多少个星,用于确定条形的高度.
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])  # 在循环中,将项目的名称附加到列表的末尾
    stars.append(repo_dict['stargazers_count'])  # 将获得的星数附加到列表的末尾

# 可视化
my_style = LS('#333366', base_style=LCS)  # 将其基色设置为深蓝色
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
# 样式实参:让标签绕x轴顺时针旋转45度(x_label_rotation=45),并隐藏了图例
# (show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'  # 给图表指定了标题
chart.x_labels = names  # 将属性x_labels设置为列表names

chart.add('', stars)  # 添加数据时,将标签设置成了空字符串
chart.render_to_file('python_repos.svg')
