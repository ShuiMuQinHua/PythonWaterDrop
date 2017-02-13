from urllib.parse import urlencode
import httplib2
# import urllib

def http_get_request():
        h = httplib2.Http()
        resp, content = h.request("http://www.douban.com/")
        print(resp)


def http_post_request():
    httplib2.debuglevel = 1
    h = httplib2.Http('.cache')
    data = {'UserName': 'admin','Password':"111111"}
    # add_credentials()方法的第三个参数是该证书有效的域名 你应该总是指定这个参数!
    # 如果你省略了这个参数，并且之后重用这个httplib2.Http对象访问另一个需要认证的站点，
    # 可能会导致httplib2将一个站点的用户名密码泄 漏给其他站点。
    h.add_credentials('diveintomark', 'MY_SECRET_PASSWORD', 'identi.ca')
    resp, content = h.request('http://127.0.0.1:825/Admin',
                              'POST',
                              urlencode(data),
                              headers={'Content-Type': 'application/x-www-form-urlencoded'})
    print(resp)
    # httplib2返回的数据总是字节串(bytes), 不是字符串。为了将其转化为字符串，你需要用合适的字符编码进行解码
    print(content.decode('utf-8'))

def http_post_cache_request():
    # 获取HTTP对象
    h = httplib2.Http('.cache')
    # 发出同步请求，并获取内容
    resp, content = h.request("http://127.0.0.1:825/Admin")
    print(resp)
    # print content
    print("......" * 3)
    httplib2.debuglevel = 1
    h1 = httplib2.Http('.cache')
    resp, content = h1.request('http://127.0.0.1:825/Admin')
    # 下面这句  不从缓存读取
    # resp, content = h1.request('http://www.weirdbird.net/sitemap.xml', headers={'cache-control': 'no-cache'})
    print(resp)
    print('debug', resp.fromcache)

http_post_cache_request()
http_post_request()
http_get_request()