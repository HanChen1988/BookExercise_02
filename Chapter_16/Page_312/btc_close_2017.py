from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
try:
    # Python 2.x 版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x 版本
    from urllib.request import urlopen
import json
import ssl
from pprint import pprint

# 报错信息:
# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]
# certificate verify failed: unable to get local issuer certificate
# (_ssl.c:1076)>

# 解决方案一:
# 全局取消证书验证(当项目对安全性问题不太重视时,推荐使用,可以全局取消证书的验证,简易方便）
# ssl._create_default_https_context = ssl._create_unverified_context
# 解决方案二:
# 使用ssl创建未验证的上下文，在url中传入上下文参数(当项目整体非常重视安全问题时,推荐这种方式,
# 可以局部取消证书验证）
context = ssl._create_unverified_context()

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/' \
           'btc_close_2017.json'
response = urlopen(json_url, context=context)  # 将json_url网址传入urlopen函数,
# Python就会向GitHub的服务器发送请求,GitHub的服务器响应请求后把btc_close_2017.json
# 文件发送给Python.
# 读取数据
req = response.read()  # response.read()可以读取文件数据
# 将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)  # btc_close_2017_urllib.json与btc_close_2017.json的内容是一样的.
# 加载json格式
file_urllib = json.loads(req)  # 将文件内容转换成Python能够处理的格式,与前面直接下载的
# 文件内容一致.
pprint(file_urllib)
