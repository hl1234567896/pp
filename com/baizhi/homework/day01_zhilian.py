from lxml import etree
import json
import requests

import MySQLdb
conn = MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		    # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="piaochong",          # 要使用的库名
    charset="utf8"      # 连接中使用的字符集
)
cursor = conn.cursor()  # 游标

proxies={
    'http':'116.208.52.41:9999'
}
count=0
for i in range(20):
    url='https://fe-api.zhaopin.com/c/i/sou?start=%s&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.99620415&x-zp-page-request-id=3c96690e724e4983814780e67dc0e2bd-1562140016350-702800&x-zp-client-id=3f37f35c-eb68-4e6e-b6c2-74b7169cc215'%(i*90)
    html_text = requests.get(url=url,proxies=proxies).text
    json_obj = json.loads(html_text)
    count+=1
    print(count,'*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n')

    for each_data in json_obj['data']['results']:
        url = each_data['positionURL']
        content = requests.get(url).content #手动编码二进制
        element_obj = etree.HTML(content)
        try:
            a=element_obj.xpath("//h3[@class='summary-plane__title']//text()")[0]
            b=element_obj.xpath("//span[@class='summary-plane__salary']//text()")[0]
            c=element_obj.xpath("//ul[@class='summary-plane__info']//text()")[0]
            d=('').join(element_obj.xpath("//div[@class='describtion__detail-content']//text()"))
            e=element_obj.xpath("//a[@class='company__title']//text()")[0]
            f=element_obj.xpath("//div[@class='company__description']//text()")[0]
            print(a,b,c,d,e,f)
            cursor.execute("insert into zhilian (txt1,txt2,txt3,txt4,txt5,txt6) values ('%s','%s','%s','%s','%s','%s')" % (a,b,c,d,e,f))
            conn.commit()
        except:
            pass
cursor.close()
conn.close()




    # print(element_obj.xpath('//div[@class="summary-plane__bottom"]//text()'))
    # print(element_obj.xpath('//*[@class="summary-plane__info"]//text()'))
    # print(element_obj.xpath('//div[@class="describtion"]//text()'))
    # print(element_obj.xpath('//a[@class="company__title"]//text()'))
    # print(element_obj.xpath('//*[@class="company__description"]//text()'))


# element_obj = etree.HTML(content)
# a_url_list = element_obj.xpath('//a[@class="contentpile__content__wrapper__item__info"]')
# print(a_url_list,len(a_url_list))
#
# '''
# 第一页
# https://sou.zhaopin.com/?jl=530&kw=python&kt=3&sf=0&st=0
# 第二页
# https://sou.zhaopin.com/?p=2&jl=530&kw=python&kt=3&sf=0&st=0
# '''


# from urllib import request
# import gzip
# headers = {
#     'accept-encoding': 'gzip'
# }
# url='https://jobs.zhaopin.com/CC442548133J00221073106.htm'
# req = request.Request(url=url,headers=headers)
# resp=request.urlopen(req)
# aa=resp.read()
# print(gzip.decompress(aa).decode('utf-8'))

