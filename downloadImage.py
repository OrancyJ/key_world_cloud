#-*- coding:utf-8 -*-
import re
import requests
# 爬取网络图片
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1511800271332_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1511800271332%5E00_1679X841&word=%E5%A5%B3%E4%BC%98'


html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print(each)
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
        continue
    string = './pictures/'+str(i) + '.jpg'

    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i += 1å

