import requests
from lxml import etree
from com.baizhi.Python161.人人网.mysql import mysql_w as sql
from com.baizhi.Python161.人人网.chaojiying import getcode

url = 'http://www.renren.com/880792860/profile'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': 'anonymid=jy3r5apouscleg; depovince=BJ; _r01_=1; JSESSIONID=abctxQ1dCCatvf7TOzZVw; ick_login=eea47ab4-b652-49f0-a89d-54cf0a9fe4ba; loginfrom=null; jebe_key=730d7a46-1649-4eaf-93f6-d16f1b2277e0%7Cc9648fadd971497f6415b29ba7925b4e%7C1563156741964%7C1%7C1563156742888; wp_fold=0; l4pager=0; t=78902bc85fa2c6ceb8235b0abf078a193; societyguester=78902bc85fa2c6ceb8235b0abf078a193; id=971493283; xnsid=aec7a81; ver=7.0; jebecookies=3bbe4336-5936-48b5-aee1-539f77fd3357|||||; jebe_key=730d7a46-1649-4eaf-93f6-d16f1b2277e0%7C7cd398382ecaca482bfadc4aea56368c%7C1563184794434%7C1'

}


def urls(url):
    with requests.session() as s:
        res = s.get(url=url,headers=headers)
        e = etree.HTML(res.text)
        friend_urls = e.xpath('//*[@id="specialfriend-box"]/div/div[1]/ul/li/a')
        user_name = ''.join(e.xpath('//*[@id="cover"]/div[2]/h1/text()')).strip()
        try:
            user_school = ''.join(e.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'))
        except:
            user_school = '无'
        try:
            user_sex = ''.join(e.xpath('//*[@id="operate_area"]/div[1]/ul/li[2]/span[1]/text()'))
        except:
            user_sex = '无'
        try:
            user_addr = ''.join(e.xpath('//*[@id="operate_area"]/div[1]/ul/li[3]/text()'))
        except:
            user_addr = '无'
        try:
            user_bir = ''.join(e.xpath('//*[@id="operate_area"]/div[1]/ul/li[2]/span[2]/text()'))
        except:
            user_bir = '无'
        try:
            code = e.xpath('//label[@for="code"]/text()')[0]
        except:
            code = ''


        print(user_name, user_school, user_sex, user_addr, user_bir)
        print(code)
        # print(res.text)
        code_res = s.get(url='http://www.renren.com/validateuser.do?id=880792860',headers=headers)
        e1 = etree.HTML(code_res.text)
        if '验证码:' == code:
            print(res.text)
            # img_src = e1.xpath('//img/@src')[1]
            img_src = 'http://icode.renren.com/getcode.do?t=ninki&rnd=1563186658140'
            print(img_src)
            with open('t.jpg','wb') as w:
                w.write(s.get(url=img_src).content)
            with open('t.jpg','rb') as r:
                im = r.read()
            c = getcode(im)['pic_str']
            print(c)
            data = {
                'id':880792860,
                'icode' : c,
                'submit': '继续浏览',
                'requestToken': '1877362478',
                '_rtk': '3ba74588'
            }
            print(data)
            res = s.post(url='http://www.renren.com/validateuser.do',data=data)
            res_people = s.get(url='http://www.renren.com/254502398/profile',headers=headers)
            print(res_people.text)
            # print(res.text)

        for friend_url in friend_urls:
            friend_url = friend_url.xpath('./@href')[0]
            print(friend_url)
            try:
                my_sql(friend_url)
                sel_sql()
            except Exception as a:
                print(a)
                continue


def my_sql(url,starts='0'):
    conn = sql('crawler')
    cursor = conn.cursor()
    cursor.execute('insert into t_urls(urls,starts) values (%s,%s)',(url,starts))
    conn.commit()
    cursor.close()
    conn.close()


def sel_sql():
    conn = sql('crawler')
    cursor = conn.cursor()
    cursor.execute('select urls from t_urls where starts=0')
    try:
        sql_url = cursor.fetchall()[-1][0]
    except:
        sql_url = ''
    if not sql_url:
        sql_url = url
    print('=============')
    print(sql_url)
    urls(sql_url)


# def save_info(*args):
#     conn = sql('zhilian')
#     cursor = conn.cursor()
#     cursor.execute('insert into t_user values (%s,%s,%s,%s,%s)', *args)
#     conn.commit()
#     cursor.close()
#     conn.close()

#
# def update_sql(url):
#     conn = sql('zhilian')
#     cursor = conn.cursor()
#     cursor.execute('update t_user set starts=1 where url="%s"'%url)
#     conn.commit()
#     cursor.close()
#     conn.close()


def main():
    sel_sql()


if __name__ == '__main__':
    main()