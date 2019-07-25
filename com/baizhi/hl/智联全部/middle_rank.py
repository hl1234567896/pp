import requests
from lxml import etree
import MySQLdb


def formatColonString(input: str) -> dict:  #把字符串转成字典
    lines = input.strip().split('\n')
    output = dict()
    for line in lines:
        if not line or line == '(empty)':
            continue
        try:
            k, v = line.split(':')
            output[k.strip()] = v.strip()
        except Exception as e:
            return {'error': e}
    return output


conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'piaochong',
    charset = 'utf8'
)
url='https://fe-api.zhaopin.com/c/i/sou'

start = 0
kw = ['python','python全栈','python爬虫','AI',' web开发','大数据','UI设计师','java','区块链','产品经理','Hadoop','PHP','数据架构']
citys=['530','538','765','763','531','801','653','736','600','613','635','702','703','639','599','854','719','749','551','622','636','654','681','682','565','664','773']
count=0
kw_index=0
city_index=0

while True:
    cursor = conn.cursor()
    sql = "select kw from journal"
    cursor.execute(sql)
    kw_index2 = cursor.fetchall()[0][0]
    print(kw_index2,'kw')
    kw_index = int(kw_index2)
    city2 = cursor.execute("select cityID from journal")
    city_index2 = cursor.fetchall()[0][0]
    print(city_index2,'city')
    city_index = int(city_index2)
    sta = cursor.execute("select start from journal")
    start2 = cursor.fetchall()[0][0]
    print(start2,'start')
    start = int(start2)
    headers={'user - agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.100Safari / 537.36'
    }
    cookies={
        'cookie':'sou_experiment=unexperiment; acw_tc=2760821415619901155598097e4d61e3270b873ef3fb44bc323304ba2301a3; x-zp-client-id=bb5f28e9-1912-49f0-9147-a742ff9bc5de; ZP_OLD_FLAG=false; sts_deviceid=16bae16e0245eb-0a35cf7514b9a3-3b654406-2073600-16bae16e0258c2; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; bdshare_firstime=1562114451678; _jzqx=1.1562114452.1562114452.1.jzqsr=jobs%2Ezhaopin%2Ecom|jzqct=/beijing/.-; adfbid2=0; registerGroup=capi; smidV2=2019070319085616296efe768ee6e72332d4cc9754908400888e248056cd010; _jzqa=1.2680979665792171500.1562114452.1562114452.1562403989.2; _jzqy=1.1562403989.1562403989.1.jzqsr=baidu.-; _qzja=1.1713552324.1562114451748.1562114451749.1562403988740.1562114451749.1562403988740.0.0.0.2.2; select_city_code=2013; select_city_name=%E6%98%8C%E5%B9%B3%E5%8C%BA; JSloginnamecookie=18311375365; JSShowname=""; at=0fd84fe9680e4013b9cbb3a31437798c; rt=041581558e0d4c879754c78deff61fe1; JSpUserInfo=3d753d6857645e7541685d645b754068526451754e685b645375356824645575486852645b7548685b645b754e685f645b754f685f6453753c6827645575486852645b7548685b645b754e685f645b754f685f64287548685c645b75576809640775146851643b752d685764597542682b643c7544685c64457549684a6459754e685064507542682b64247544685b6453752c682b6455753368276450754e6859645175416853645f754868536453752c683e645575486851643b7530685764587542683; uiioit=3d753d6a44640f38536d596205355d684d7953795339096b566e203671645575496a42649; adfcid2=none; urlfrom=121113803; urlfrom2=121113803; adfbid=0; sts_sg=1; sts_sid=16bcf012b4156a-0fe7fe5dea00d8-3a65420e-2073600-16bcf012b4242c; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsabWzFI00000r2_AdC00000v3qM8C.THLyktAJ0A3qmh7GuZR0T1d-mhmkrjD1nj0sPj9-mynd0ZRqwHnLnjFjPbfknWIjrHbkrH9KrH6swj6kwWNAwHTswjD0mHdL5iuVmv-b5HnznWcvnWR3rjmhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh99ULKGUB4WUvYOTv-b5HDznHDkn16snzudIAdxTvqdThP-5yF9pywdTAPsXBudIAdxUyNbpgNV5yPsI0KWThnqPWRzrjT%26tpl%3Dtpl_11535_18778_14772%26l%3D1511763170%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3222625886_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D241%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%2599%25BA%25E8%2581%2594%26rqlang%3Dcn%26inputT%3D2009; dywea=95841923.1446049912329155300.1562077393.1562510206.1562546089.15; dywec=95841923; dywez=95841923.1562546089.15.12.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic|dywectr=%25E6%2599%25BA%25E8%2581%2594; dyweb=95841923.1.10.1562546089; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22687398971%22%2C%22%24device_id%22%3A%2216bae16e045973-038d7098fe4191-3b654406-2073600-16bae16e0468b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsabWzFI00000r2_AdC00000v3qM8C.THLyktAJ0A3qmh7GuZR0T1d-mhmkrjD1nj0sPj9-mynd0ZRqwHnLnjFjPbfknWIjrHbkrH9KrH6swj6kwWNAwHTswjD%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%22%2C%22%24latest_utm_source%22%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22tj%22%2C%22%24latest_utm_term%22%3A%2228700001%22%7D%2C%22first_id%22%3A%2216bae16e045973-038d7098fe4191-3b654406-2073600-16bae16e0468b7%22%7D; __utma=269921210.1961658182.1562077394.1562509389.1562546089.14; __utmc=269921210; __utmz=269921210.1562546089.14.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E6%99%BA%E8%81%94; __utmt=1; __utmb=269921210.1.10.1562546089; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1562479327,1562509389,1562510207,1562546089; jobRiskWarning=true; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1562546097; acw_sc__v2=5d228fb52d2dd36487834e9896ed22f5e7c13947; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22d2f857c7-447b-4848-a77b-c82d9756d9da-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22f0711ad0-fd9e-45ce-a55b-e8704f0c1fb5-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_evtseq=6'
    }
    params = {
        'start': start2,
        'pageSize': 90,
        'cityId': citys[int(city_index2)],
        'workExperience': -1,
        'education': -1,
        'companyType': -1,
        'employmentType': -1,
        'jobWelfareTag': -1,
        'kw': kw[int(kw_index2)],
        'kt': 3,
        '_v': 0.05792497,
        'x-zp-page-request-id': '74540f58ed244a73965566c159408b4a-1562326642728-154598',
        'x-zp-client-id': '89522732-6641-494e-8b65-d9381d5c9ab2'
    }
    try:
        with requests.session() as s:
            res = s.get(url=url,params=params,headers=headers,cookies=cookies)
            data = res.json()['data']
            datas = data['results']
            # print(datas,64)
            count = int(data['count'])
            # print(count,66)
            for i in datas:
                # print(requests.get(url=i['positionURL']).text)
                try:
                    # print(i['positionURL'])
                    elem = etree.HTML(s.get(url=i['positionURL'],timeout=2,headers=headers,cookies=cookies).text)
                    # print(s.get(url=i['positionURL'],timeout=2).text)
                    jobName = ''.join(elem.xpath('//h3[@class="summary-plane__title"]/text()'))
                    salary = elem.xpath('//span[@class="summary-plane__salary"]/text()')[0]
                    print(salary)
                    city = ''.join(elem.xpath('//a[@href="//www.zhaopin.com/beijing/"]/text()')[0])
                    print(city)
                    data = elem.xpath('//ul[@class="summary-plane__info"]/li/text()')[0]
                    print(data)
                    company = elem.xpath('//a[@class="company__title"]/text()')[0]
                    print(company)
                    company_des = elem.xpath('string(//div[@class="company__description"]/text())')
                    print(company_des)
                    description = elem.xpath('string(//div[@class="describtion"])')
                    sql2 = 'insert into employment_copy(position,salary,address,gzyq,job_description,company_name,company_profile) values ("%s","%s","%s","%s","%s","%s","%s")'
                    cursor.execute(sql2 % (jobName,salary,city,data,description,company,company_des))
                    conn.commit()
                    print('---------------------')
                except Exception as e:
                    print(e)
            start += 90
            cc = "update journal set start="+str(start)+""
            cursor.execute(cc)
            conn.commit()
            print('*************************下一页')
            print(start,count)
    except:
        pass
    if start >= count:
        print(start,count,'111111111')
        #更换关键字
        kw_index += 1
        command = "update journal set kw="+str(kw_index)+""
        cursor.execute(command)
        conn.commit()
        start = 0
        cc = "update journal set start=" + str(start) + ""
        cursor.execute(cc)
        conn.commit()
        if kw_index >= len(kw):
            #更换城市
            city_index += 1
            kw_index = 0
            command1 = "update journal set kw="+str(kw_index)+""
            cursor.execute(command1)
            conn.commit()
            command2 = "update journal set cityID="+str(city_index)+""
            cursor.execute(command2)
            conn.commit()
            start = 0
            if city_index >= len(citys):
                break
                cursor.close() #先关闭cursor
                conn.close()