import urllib.request
import urllib.parse
import json

# 百度翻译url，寻找请求地址，
url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# fromdata 在network - payload一栏
data = {
    'kw': 'spider'
}
# post请求必须进行utf-8编码,否则TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
data = urllib.parse.urlencode(data).encode('utf-8')
print(data)

# post请求必须加入data，不可拼接 encode编码
request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)
# decode解码
content = response.read().decode('utf-8')
print(content)

res = json.loads(content)
print(res)