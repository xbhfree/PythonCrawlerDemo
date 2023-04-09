import urllib.request

# 文件下载示例

# 下载网页
# url_page = 'http://www.baidu.com'
# urlretrieve(url, filename)  url代表下载路径，filename文件的名字
# retrieve 找回，收回；检索（储存于计算机的信息）
# urllib.request.urlretrieve(url_page, 'baidu.html')


# 下载图片
# url_image = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw1%2F0ec01d5c-862d-45f7-91b3-17456cdc52d6%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1683636401&t=91d319caa0251ea723a767cf9a4740e7'
# urllib.request.urlretrieve(url=url_image, filename='mypage2.png')

# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-mk9yr6rr23dbes6n/cae_h264/1636585706129548942/mda-mk9yr6rr23dbes6n.mp4?v_from_s=hkapp-haokan-hnb&auth_key=1681046287-0-0-0b025fe0415603803222809a2a1d6edf&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=2886798393&vid=9150063436918367577&abtest=107353_1-109133_1&klogid=2886798393'
urllib.request.urlretrieve(url=url_video, filename='myvideo.mp4')