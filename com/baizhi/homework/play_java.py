import json
import requests
from lxml import etree
import MySQLdb

conn=MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		    # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="piaochong",          # 要使用的库名
    charset="utf8"      # 连接中使用的字符集
)
cursor=conn.cursor()    #游标

proxies={
    'http':'115.115.3.167:9999'
}

count=0
for a in range(20):
    url='https://fe-api.zhaopin.com/c/i/sou?start=%s&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&=0&_v=0.21002723&x-zp-page-request-id=919373cf21e3427a845e6f7e1100b72f-1562233910852-232105&x-zp-client-id=3f37f35c-eb68-4e6e-b6c2-74b7169cc215' % (90*a)
    txt_html = requests.get(url=url,proxies=proxies).text
    str_html = json.loads(txt_html)
    count+=1
    print('\n*\n*\n*\n*\n*\n*','下面是第',count,'页的数据','\n*\n*\n*\n*\n*\n*')

    for i in str_html['data']['results']:
        small_url=i['positionURL']
        print(small_url)
        content=requests.get(small_url).content   #转为二进制
        ele = etree.HTML(content)   #<Element html at 0x32aca88>
        try:
            a=ele.xpath("//h3[@class='summary-plane__title']//text()")[0]
            b=ele.xpath("//span[@class='summary-plane__salary']//text()")[0]
            c=("-").join(ele.xpath("//ul[@class='summary-plane__info']//text()"))
            d=("-").join(ele.xpath("//div[@class='highlights']//text()"))
            e=('').join(ele.xpath("//div[@class='describtion']//text()"))
            f=ele.xpath("//a[@class='company__title']//text()")[0]
            g=ele.xpath("//div[@class='company__description']//text()")[0]
            print(a,b,c,d,e,f,g)
            cursor.execute("insert into java2 (t1,t2,t3,t4,t5,t6,t7) values ('%s','%s','%s','%s','%s','%s','%s')" % (a,b,c,d,e,f,g))
            conn.commit()
        except:
            pass
cursor.close()
conn.close()



#没网爬你妈








# a={
# Bdpagetype:3,
# Bdqid:0x99759627003abfa7,
# Cache-Control:private,
# Ckpacknum:2,
# Ckrndstr:7003abfa7,
# Connection:Keep-Alive,
# Content-Encoding:gzip,
# Content-Type:text/html;charset=utf-8,
# Date:Wed, 17 Jul 2019 01:01:41 GMT,
# P3p:CP=" OTI DSP COR IVA OUR IND COM ",
# Server:BWS/1.1,
# Set-Cookie:BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; path=/; domain=.baidu.com,
# Set-Cookie:delPer=0; path=/; domain=.baidu.com,
# Set-Cookie:BD_CK_SAM=1;path=/,
# Set-Cookie:PSINO=1; domain=.baidu.com; path=/,
# Set-Cookie:BDSVRTM=11; path=/,
# Set-Cookie:H_PS_PSSID=1432_21102_29522_29519_28518_29098_28837_29221_22157; path=/; domain=.baidu.com,
# Strict-Transport-Security:max-age=172800,
# Transfer-Encoding:chunked,
# Vary:Accept-Encoding,
# X-Ua-Compatible: IE=Edge,chrome=1

# }
#











