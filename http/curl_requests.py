import requests
from requests.auth import HTTPBasicAuth
import urllib.request
import json

def get():
    print(requests.get("http://www.baidu.com"))

def post_with_auth():
    url = 'http://127.0.0.1:825/Admin'
    r = requests.post(url, data={}, auth=HTTPBasicAuth('admin', '111111'))
    print(r.status_code)
    print(r.headers)
    print(r.reason)

def douban_api_culr():
    html = urllib.request.urlopen(r'https://api.douban.com/v2/book/isbn/9787218087351')
    ret = html.read()
    print(ret.decode('utf-8'))
    hjson = json.loads(ret.decode('utf-8'))  #ret.decode('utf-8')  字节转换为字符串

    print(hjson['rating'])
    print(hjson['images']['large'])
    print(hjson['summary'])

get()
post_with_auth()
douban_api_culr()