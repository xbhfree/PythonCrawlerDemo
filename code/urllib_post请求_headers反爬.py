import urllib.request
import urllib.parse
import json
# find what       (.*):(.*)
# replace with    '\1':'\2',
# 勾选 regular expression;notify end of file; current file
# editplus 正则可以快速替换加 ''
#
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept':' */*',
    # 不注释，会有编码问题
    #'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':' zh-CN,zh;q=0.9',
    'Acs-Token':' 1682256485016_1682256508566_qROef3E8E/vAXgW6rNkmxsY0guCsCoy+d5ELrhgqSSTeC4Icopac2X7MekYTW1Lk0K/sAu+ZX88qcQ5abv7+gbhtsliL/y9k1DANhvIu5+00ZmvqdVfkE68KBuqvwVbakBgkFCQMFYB2gfQao8KUFbUyhhKnW0zL6Fw/j4XI6MQn6oz+tP8tErd3v1F1Vvvsd49DrdXoVHcq4PyRs6AGRea7wawn6hB0WxFTybWtsDVrlOF95hPuC28aLqAXizP0cp5+JfPqrKscnVBffHdSChcq6itycQjruWSEIWbhDmfzfPmVlv7kXHgO8v6J98tLG9hkRny3yzift+utxMwpjkh357kmFHGxr/zSFnK86vtsCszFi2f+cKmrHw4pj6tGPjYkiLjQhCg+3et156lsbEiNu2E9i5s4FCKnaLbO/0rpf1gTtoNO2rws271ataRbDUmCgdNRapvOPc3s9mNkIRqDA3caNY8M7ooG5H7Bb1ek/B9bmvv/8G5lkp7STUJa',
    'Connection':' keep-alive',
    'Content-Length':' 135',
    'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
    # cookie为关键信息
    'Cookie': 'BIDUPSID=FB2EBF52F9FAA2BFE19084E29FE40F73; PSTM=1673356315; BAIDUID=FB2EBF52F9FAA2BFC94CBC74113CCA1A:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; newlogin=1; APPGUIDE_10_0_2=1; H_PS_PSSID=38515_36548_38470_38354_38364_38468_38376_38485_37927_37709_38507_26350_22160; delPer=0; PSINO=5; BAIDUID_BFESS=FB2EBF52F9FAA2BFC94CBC74113CCA1A:FG=1; BA_HECTOR=aka10ha121ala400040hak851i4ac031m; ZFY=8wo3tcoD7qbVxlgQEJ:BgmUurHLtDekXfmmzizEKPih8:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=11072791858063427870; BCLID_BFESS=11072791858063427870; BDSFRCVID=LDkOJexroG07VWbfOHRCbcdC8LweG7bTDYrEOwXPsp3LGJLVFe3JEG0Pts1-dEu-S2OOogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=LDkOJexroG07VWbfOHRCbcdC8LweG7bTDYrEOwXPsp3LGJLVFe3JEG0Pts1-dEu-S2OOogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsWU3WB2Q-XPoO3KtbSx3Pbxn10xtV-UOmqU7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0tLeWeTxoUJ2-KDVeh5Gqq-KXU4ebPRiB-b9QgbA5hQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj-hD6c33D; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsWU3WB2Q-XPoO3KtbSx3Pbxn10xtV-UOmqU7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0tLeWeTxoUJ2-KDVeh5Gqq-KXU4ebPRiB-b9QgbA5hQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj-hD6c33D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1681737346,1682256485; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1682256485; ab_sr=1.0.1_M2RmNWU0ZGE3NTYzNWVjNDY3YmEwMzdkMDY4ZWNhZDBjMmU0NjhlMzVjYzE5ODVhYzE1Yzk5ZWYwZDM4ZmEyOTExYjgyNDc3YWM0ZjFjYTgxNDhmYjdmYzQ3Y2M3MDg4MGM5YzhjM2MwNmNmZGUyMzlkYmExZmY1OTcxODIwMmE4MWRlNTc1YWQxZWM5MWZhYmQ2OTZhYjE4NjRmMTg1NA==',
    'Host':'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':' empty',
    'Sec-Fetch-Mode':' cors',
    'Sec-Fetch-Site':' same-origin',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Requested-With':' XMLHttpRequest'
}

data = {
    'from':'en',
    'to':'zh',
    'query':'love',
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'198772.518981',
    'token':'f9284f3a22a099bccec740e11788914e',
    'domain':'common'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url = url, data = data, headers = headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
res = json.loads(content)
print(res)