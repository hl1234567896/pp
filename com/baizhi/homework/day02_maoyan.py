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


import  requests
from  lxml import etree
# url='https://maoyan.com/board/4?offset=0'
# url='https://maoyan.com/board/4?offset=10'
all_url = 'https://maoyan.com'
url_big = ['https://maoyan.com/board/4?offset=%s' % (count*10) for count in range(10)]
for url in url_big:
    html_text = requests.get(url).text
    element_obj = etree.HTML(html_text)
    href_list = element_obj.xpath('//a[@data-act="boarditem-click"][@class]/@href')
    for i in  href_list:
        detail_page_html = requests.get(all_url + i).text
        detail_page_obj = etree.HTML(detail_page_html)
        a=detail_page_obj.xpath('//h3[@class]/text()')[0]
        b=detail_page_obj.xpath('//div[@class="movie-brief-container"]/ul/li[1]/text()')[0]
        k=detail_page_obj.xpath('//div[@class="movie-brief-container"]/ul/li[2]/text()')[0].replace('\n','').replace(' ','')
        d=detail_page_obj.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')[0]
        print(a,b,k,d)
#         cursor.execute("insert into maoyan (movie_name,movie_type,movie_country,times) values ('%s','%s','%s','%s')" % (a,b,k,d))
#         conn.commit()
#
# cursor.close()
# conn.close()















# import urllib.request as ur
# import re
# url='https://maoyan.com/board/4?offset=0'
# # url='https://maoyan.com/board/4?offset=10'
# res=ur.urlopen(url=url)
# res1=res.read().decode('utf-8')
# '<a href="/films/14556" title="大闹天宫" class="image-link" data-act="boarditem-click" data-val="{movieId:14556}"></a>'
#
# rule_list='<a href="(.*?)" title=".*?" class="image-link" '
#
# url_list=re.findall(rule_list,res1)
# print(url_list)
# urllist=['https://maoyan.com'+i for i in url_list]
# count=0
# for a in urllist:
#     res1=ur.urlopen(url=url)
























