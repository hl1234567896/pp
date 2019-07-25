import json
import requests
from lxml import etree
import MySQLdb
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'piaochong',
    charset = 'utf8'
)
cursor=conn.cursor()
url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA&pn={}&rn=10&ie=utf-8&oe=utf-8&format=json&t=1562397160646&cb=jQuery110208881246287684195_1562397048320&_=1562397048323'
params = {
'resource_id': 6899,
'query': '失信人',
'pn': 10,
'rn': 10,
'ie': 'utf-8',
'oe': 'utf-8',
'format': 'json',
't': 1562337275362,
'cb': 'jQuery110203414624977161749_1562337189630',
'_': 1562337189632,
}



headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Referer': 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&oq=httpbin%25E6%25B5%258B%25E8%25AF%2595&rsv_pq=92bc155b000b8790&rsv_t=3da1nUFM1zHNhggXVC7Ys9IqaZhZGZ2%2BADppam4N1h1t126OoCFNNMsEDIk&rqlang=cn&rsv_enter=0&inputT=4260&rsv_sug3=26&rsv_sug1=34&rsv_sug7=100&prefixsug=%25E5%25A4%25B1%25E4%25BF%25A1%25E4%25BA%25BA&rsp=0&rsv_sug4=4260'
}


with requests.session() as  s:
    for j in range(5000):
        html_text = s.get(url=url.format(j*10),params=params,headers=headers).text
        data =''
        data1 =''
        for i in  html_text.split('(')[1:]:
            data+=i
        for k in data.split(');')[:-1]:
            data1+=k
        list_details = json.loads(data1)
        if list_details['data']:#判断是否有数据
            list_details = list_details['data'][0].get('result')
            for i in  list_details:
                name = i['iname']
                card = i['cardNum']
                gistUnit1 = i['gistUnit']
                areaNameNew = i['areaNameNew']
                caseCode = i['caseCode']
                gistId = i['gistId']
                performance = i['performance']
                duty = i['duty']
                publishDate = i['publishDate']
                print(name,card,gistUnit1,areaNameNew,caseCode,)
                sql = 'insert into shixinren values("%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(name,card,gistUnit1,areaNameNew,caseCode,gistId,performance,duty,publishDate)
                cursor.execute(sql)
                conn.commit()
    cursor.close()
    conn.close()






