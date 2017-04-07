# -*- coding: UTF-8 -*-

import json

# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data)) #repr 将任意值转为字符串(转换为供机器读取的形式)   str  将任意值转化为字符串(易于人阅读)
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

# 从文件中读取的json数据

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json_str = json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)


# 写入json文件
def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))

# 从json文件中读取数据  读取配置文件
def load():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data

data = {}
data['name'] = 'cyy'
data['age'] = '18'
store(data)

data = load()
print(data['name'])

