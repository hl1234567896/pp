# -*- coding: utf-8 -*-
import scrapy
import com.baizhi.hl.scrapy框架.job.job.items as items



class Job51Spider(scrapy.Spider):

    kws = ['python','HTML','C++','python全栈','python爬虫','AI','web开发','大数据','java','产品经理','Hadoop']
    city_id = 0
    page = 0
    kws_index = 0

    name = 'job51'  #爬虫名
    allowed_domains = ['https://jobs.51job.com']    #域名
    start_urls = ['https://www.51job.com/']    #第一次要访问的url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Cookie': 'guid=d96f753e2eb2caa30a00ef28d60a79cf; slife=lastvisit%3D010000%26%7C%26; adv=adsnew%3D1%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fsp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fDewkY0XJVb00uiAs0IIzwI000002SLnNC00000v3qM8C.THYdnyGEm6K85yF9pywd0ZnqujRLrHbkuWbsnj0Ym16zrfKd5HcYwWmzfYRLn1fsnWbsPH7jPHw7wHTdPWcsrRfzrH6v0ADqI1YhUyPGujY1nWR3nWbknWTLFMKzUvwGujYkP6K-5y9YIZK1rBtEIZF9mvR8PH7JUvc8mvqVQLwzmyP-QMKCTjq9uZP8IyYqn1DvrjbLrau9pM0qmR9inAPcHHunXH-YmHPwIR4RwM7Bnb-dyHc4IDs1Rh4nnY4_m-n4IvN_rZ-PwDRYHAdCnAFgIzqpUbGvm-fkpN-gUAVbyDcvFh_qn1u-njRYmyDsPjR4m1F-uAfdmWfLuWRLmvcvnHKbrjc0mLFW5Hn3P1Rk%2526tpl%253Dtpl_11534_19968_16032%2526l%253D1513207727%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E6%252525A0%25252587%252525E9%252525A2%25252598-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526xp%25253Did%2528%25252522m3258291277_canvas%25252522%2529%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D248%2526ie%253Dutf-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D51job%2526rqlang%253Dcn%2526inputT%253D1435%26%7C%26adsnum%3D3168978; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1562670884%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21',
        'Referer': 'https://mkt.51job.com/'
    }

    def parse(self, response):  #解析响应   在运行时会被引擎自动调用
        # response 是引擎直接返回的响应对象,是下载器间接返回的响应对象
        # response 可以直接使用xpath语法,还可以使用选择器对象

        while 1:
            self.page += 1
            if self.page >= 90:
                self.kws_index += 1
                if self.kws_index > len(self.kws) - 1:
                    self.city_id += 1
                    if self.city_id >= 10:
                        break
            url = 'https://search.51job.com/list/0{}0000,000000,0000,00,9,99,{},2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(self.city_id, self.kws[self.kws_index], self.page)

        # 发送一个请求(列表页)   发送请求 获取列表页html页面
            yield scrapy.Request(url=url,callback=self.paresListPage,headers=self.headers,dont_filter=True)


    #解析列表页的方法
    def paresListPage(self,response):
        # print('**********************************************')
        result=response.xpath('//p[@class="t1 "]/span/a/@href').extract()
        for detailURL in result:
            yield scrapy.Request(url=detailURL,dont_filter=True,callback=self.detailParse,headers=self.headers)

    def detailParse(self,response):
        # print('进入详情页')
        job_name=response.xpath('//h1/@title').extract()[0] #职位名称
        job_message=''.join(response.xpath('string(//div[@class="bmsg job_msg inbox"])').extract()[0]).replace('\t','').replace('\n','').replace(' ','')
        company_name=response.xpath('//p[@class="cname"]/a/@title').extract()[0]
        company_information=''.join(response.xpath('//div[@class="tmsg inbox"]/text()').extract()).replace('\t','').replace('\n','').replace(' ','')
        good=response.xpath('//span[@class="sp4"]/text()').extract()

        print(job_name)
        # print(job_message)
        # print(company_name)
        # print(company_information)
        # print(good)
        #将任何数据进行返回
        #任何解析方法:parse 只能返回:Request对象构成的可迭代对象(生成) Item 字典
        i=items.JobItem()
        i['job_name']=job_name
        i['job_message']=job_message
        i['company_name']=company_name
        i['company_information']=company_information
        i['good']=good
        return i    #返回了一个Item对象













