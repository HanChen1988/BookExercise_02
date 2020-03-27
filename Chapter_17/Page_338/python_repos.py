import requests

# # 增加重试连接次数
# requests.adapters.DEFAULT_RETRIES = 5
# s = requests.session()
# # 关闭多余的连接
# s.keep_alive = False

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)  # 调用get()并将URL传递给它,再将响应对象存储在变量r中.
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
print("Repositories returned:", len(repo_dicts))  # 我们打印repo_dicts的长度,以
# 获悉我们获得了多少个仓库的信息.

# 研究第一个仓库
repo_dict = repo_dicts[0]  # 为更深入地了解返回的有关每个仓库的信息,我们提取了repo_dicts
# 中的第一个字典,并将其存储在repo_dict中.
print("\nKeys:", len(repo_dict))  # 我们打印这个字典包含的键数,看看其中有多少信息.
for key in sorted(repo_dict.keys()):
    print(key)  # 我们打印这个字典的所有键,看看其中包含哪些信息.
