#coding=utf-8
import urllib.request
import urllib
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'  #正则表达式 抓取网页图片
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html.decode('utf-8'))
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)  #从远程url下载图片 保存到本地 并修改名称
        x+=1
    return x


html = getHtml("http://tieba.baidu.com/p/2460150866")
print(getImg(html))