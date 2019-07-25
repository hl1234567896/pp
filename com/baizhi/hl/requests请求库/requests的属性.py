import requests
import chardet

url='http://www.baidu.com'
res=requests.get(url)
# print(res.status_code)  #状态码
# print(res.encoding) #设置编码
# print(res.apparent_encoding)    #自动获得编码方式
# res.encoding=res.apparent_encoding  #使用requests内置编码解析方式,自动获取编码
# print(res.text) #str html源码

# print(chardet.detect(b'abc'))   #{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# print(res.content)
# res.encoding=chardet.detect(res.content)
# print(res.text)

print(res.cookies)  #<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(res.elapsed)  #0:00:00.024770
print(res.history)  #历史记录
print(res.headers)  #头信息
print(res.url)  #http://www.baidu.com/
print(res.json) #<bound method Response.json of <Response [200]>>











