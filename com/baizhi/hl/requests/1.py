import requests
import json
url='https://www.baidu.com/'
res=requests.get(url=url)
# print(res)  #<Response [200]>是一个Response对象
# print(res.text) #获得html文本 <class 'str'>
print(res.content)



