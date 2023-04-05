# urllib的其他方法
import urllib.request

url = 'http://www.baidu.com'
# 2. 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 3.获取相应页的源码
# 最前面有个b,代表返回的是字节形式的二进制代码，需要解码
# 二进制->字符串
#content = response.read().decode('utf-8')

# 打印response类型 http.client.HTTPResponse
# print('打印response类型')
# print(type(response))

# 一个一个字节读
# content = response.read()
# print(content)

# 多个字节读
# content = response.read(10)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 一行行读直到读完
# content = response.readline()
# print(content)

# 获取状态码
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# 返回状态信息
# print(response.getheaders())