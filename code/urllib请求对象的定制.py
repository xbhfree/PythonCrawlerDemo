import urllib.request

# url 构成：
#  http https  www.baidu.com     8080      /s   wd=alisa   #
#   协议            主机          端口号      路径    参数      锚点
url = 'https://www.baidu.com'
# 传入ua，解决ua反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# 请求对象的定制，必须写url=,header=，因为简写第二个是date
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

