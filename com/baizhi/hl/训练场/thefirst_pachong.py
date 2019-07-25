import re
import urllib.request as ur
# url='https://tieba.baidu.com/f?kw=%s'
# res=ur.urlopen(url)
# print(res.read().decode('utf-8'))
# res=ur.urlretrieve(url=url,filename='hehe.html')    # urlretrieve 向服务器发送请求，并将响应存储到本地

kw='桌面'
kw=ur.quote(kw)
url='https://tieba.baidu.com/f?kw=%s'%kw
res=ur.urlopen(url=url)
res11=res.read().decode('utf-8')
'''
<img class="BDE_Image" pic_type="0" width="560" height="349" src="https://imgsa.baidu.com/forum/w%3D580/sign=3b88ddc1b712c8fcb4f3f6c5cc0292b4/5d2662d0f703918fe9ef922b5f3d269759eec412.jpg"><a rel="noreferrer" href="/p/6170785674" title="自己画的也可以用来做桌面哦~" target="_blank" class="j_th_tit ">自己画的也可以用来做桌面哦~</a>
<a rel="noreferrer" href="/p/6171161559" title="求这个win10电脑锁屏的壁纸，找了一下午了没找到…" target="_blank" class="j_th_tit ">求这个win10电脑锁屏的壁纸，找了一下午了没找到…</a>
j_th_tit 
'''

# rule='<img class="BDE_Image" src="(.*?)"'

rule='<a.*?href="(.*?)" title.*?class="j_th_tit "'
print(rule)
urllist1=re.findall(rule,res11)
print(urllist1)
urllist=['https://tieba.baidu.com'+i for i in urllist1]
count = 0
for url in urllist:
    res1=ur.urlopen(url=url)
    rule2='<img.*? src="(.*?\.jpg)"'
    print(rule2)
    try:
        imgPage=res1.read().decode()
        res2=re.findall(rule2,imgPage)
        for i in res2:
            count+=1
            ur.urlretrieve(url=i,filename='%s.jpg'%count)
    except:
        pass
ur.urlcleanup()


#网不好 只有这么多

