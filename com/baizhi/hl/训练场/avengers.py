import re
import urllib.request as ur
url='http://tieba.baidu.com/f?kw=%E5%A4%8D%E4%BB%87%E8%80%85%E8%81%94%E7%9B%9F' #访问并获取响应
res=ur.urlopen(url) #开启一个流 二进制流
print(res.read().decode('utf-8'))   #打印网页前端代码























