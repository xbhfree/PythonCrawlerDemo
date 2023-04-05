# urllib测试demo

import urllib.request


# 基础使用
def urllibBase():
    # 1.定义一个url
    url = 'http://www.baidu.com'
    # 2. 模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(url)
    # 3.获取相应页的源码
    # 最前面有个b,代表返回的是字节形式的二进制代码，需要解码
    # 二进制->字符串
    content = response.read().decode('utf-8')
    # 4. 打印数据
    print(content)

# urllibBase()
