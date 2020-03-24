import requests
# import btc_close_2017

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/' \
           'btc_close_2017.json'
req = requests.get(json_url)  # requests通过get方法向GitHub服务器
# 发送请求.GitHub服务器响应请求后,返回的结果存储在req变量中.
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)  # req.text属性可以直接读取文件数据,返回格式是字符串.
file_requests = req.json()  # 直接用req.json()就可以将btc_close_2017.json文件的数据
# 转换成Python列表file_requests.
# print(btc_close_2017.file_urllib == file_requests)  # file_urllib与
# file_requests内容相同
print(file_requests)
