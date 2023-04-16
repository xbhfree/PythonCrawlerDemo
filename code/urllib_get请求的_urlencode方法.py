import  urllib.request
import  urllib.parse
# 解决urllib.parse.quote只能单个转码问题


data = {
    'wd': '周杰伦',
    'sex': '男'
}
url = 'https://www.baidu.com/s?'
result = urllib.parse.urlencode(data)
url = url + result
print(result)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url= url, headers=headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)
