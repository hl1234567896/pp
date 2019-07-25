from lxml import etree
import json
import requests
import MySQLdb
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user="root",
    password="123456",
    db="piaochong",
    charset="utf8"
)
cursor = conn.cursor()

url='http://www.renren.com/880151247/profile'
headers={
    'Cookie': 'anonymid=jy3susa9-hb0quy; depovince=BJ; _r01_=1; jebe_key=497c101a-507c-4d85-abca-5f5d2a83c840%7Cd861fc849e1c3a5222a7527510f4ceec%7C1563159652687%7C1%7C1563159652824; jebe_key=497c101a-507c-4d85-abca-5f5d2a83c840%7Cd861fc849e1c3a5222a7527510f4ceec%7C1563159652687%7C1%7C1563159652827; JSESSIONID=abc6wzMiBXrsjcWtp90Vw; ick_login=6d04a77b-d755-43e2-bfb5-a9cb0df78411; t=ebec63e45692e1bb6403b155afaba2987; societyguester=ebec63e45692e1bb6403b155afaba2987; id=971493247; xnsid=b0adab4; ver=7.0; loginfrom=null; wp=1; wp_fold=1; XNESSESSIONID=45edf01c4fdc; jebecookies=99bd6830-5756-4237-9e2c-2b37d12185a8|||||',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
}

def urls(url):
    res=requests.get(url=url,headers=headers)
    # print(res)
    element_text=etree.HTML(res.text)
    # print(element_text)
    come=element_text.xpath('//div[@id="footprint-box"]//a//@href')
    # print(come)
    namecard=element_text.xpath('//div[@id="footprint-box"]//a/@namecard')
    # print(namecard)
    user_name=(''.join(element_text.xpath('//*[@id="cover"]/div[2]/h1/text()'))).strip()
    try:
        user_school=element_text.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')[0]
    except:
        user_school='没'
    try:
        user_sex=element_text.xpath('//*[@id="operate_area"]/div[1]/ul/li[2]/span[1]/text()')[0]
    except:
        user_sex='没'
    try:
        user_address=element_text.xpath('//*[@id="operate_area"]/div[1]/ul/li[3]/text()')[0]
    except:
        user_address='没'
    try:
        user_birth=''.join(element_text.xpath('//*[@id="operate_area"]/div[1]/ul/li[2]/span[2]/text()'))[1:]
    except:
        user_birth='没'

    print(user_name,user_school,user_sex,user_address,user_birth)
    for i in come:
        # print(i)
        try:
            cursor.execute('insert into renren values ("%s","%s")'%(i,1))
            conn.commit()
        except:
            pass
    else:
        out_url='select t_url from renren where zhuangtai=1'
        cursor.execute(out_url)
        result=cursor.fetchone()[0]
        print(result)
        cursor.execute('update renren set zhuangntai=0 where t_url=%s'%result)
        conn.commit()
        urls(result)
urls(url)























