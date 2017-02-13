import urllib.request
import urllib

def http_request_get1(url):
    response = urllib.request.urlopen(url)
    print(response.read())
    #print response.getheaders()

def http_request_post1(url):
    post_data = urllib.parse.urlencode({'a':"test"})
    req = urllib.request.Request(url + '?' + post_data)
    response = urllib.request.urlopen(req)
    print(response.read())
    # the_page = response.read()
    # print(the_page.decode('UTF8'))
    #print response.getheaders()

url = "http://www.baidu.com"
http_request_get1(url)
http_request_post1(url)