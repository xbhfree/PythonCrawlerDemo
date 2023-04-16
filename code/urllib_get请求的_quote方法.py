import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd=周杰伦'
url2 = 'https://www.baidu.com/s?wd='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# get请求方式中对超出ascii的转换处理 转换成unicode编码
name = urllib.parse.quote('周杰伦')
url2 = url2 + name
print(name)


request = urllib.request.Request(url = url2, headers= headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)