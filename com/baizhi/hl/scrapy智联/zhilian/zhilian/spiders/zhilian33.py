# -*- coding: utf-8 -*-
import scrapy, json, requests, json, re, urllib
from ..items import ZhilianItem
from urllib import parse

import time

class Zhilian33Spider(scrapy.Spider):
    name = 'zhilian33'  #爬虫名
    allowed_domains = ['https://www.zhaopin.com/']  #域名
    start_urls = ['https://www.zhaopin.com/']   #第一次要访问的url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'cookie':'adfbid2=0; x-zp-client-id=3f37f35c-eb68-4e6e-b6c2-74b7169cc215; registerGroup=capi; sts_deviceid=16baddfa701121-0e21888b11efa4-3c3c5905-1327104-16baddfa702b76; sou_experiment=unexperiment; acw_tc=2760829515619912440317056e86d265e95adcf4d063c8e9039069e47cc1f8; adfcid2=none; _jzqa=1.3513963075390130700.1561994968.1561994968.1561994968.1; _qzja=1.1609479764.1561994968570.1561994968570.1561994968571.1561994968570.1561994968571.0.0.0.1.1; dywez=95841923.1562121077.2.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utmz=269921210.1562121077.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; smidV2=2019070319543839ae26ca99ae6421dac8b23b57499a4d00c3c3620daa8e6c0; urlfrom2=121126445; ZP_OLD_FLAG=false; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D95LCPXK2McIYoccWwD1seF08WI5GjqOe4heR_EnGVB5hKKlTERvoNOvt9EIMBoBg%26wd%3D%26eqid%3Df238eea8000016c8000000025d2adb2f; jobRiskWarning=true; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1563083345,1563085917,1563087508,1563089714; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216bea1d8542394-0df688357d5f56-404b032d-1327104-16bea1d8543544%22%2C%22%24device_id%22%3A%2216bea1d8542394-0df688357d5f56-404b032d-1327104-16bea1d8543544%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _uab_collina=156309084892201694642541; sts_sid=16befcfd343703-0f5c006e2537a5-404b032d-1327104-16befcfd34487b; dywec=95841923; __utmc=269921210; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; acw_sc__=5d2b0fe59d80e73a2accef3df9df35e326c5fbff; dywea=95841923.1227210492497372400.1561994967.1563100485.1563104025.11; __utma=269921210.42370481.1561994968.1563100485.1563104025.10; __utmt=1; urlfrom=121126445; adfcid=none; adfbid=0; dyweb=95841923.2.10.1563104025; __utmb=269921210.2.10.1563104025; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1563104588; ZL_REPORT_GLOBAL={%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%22853d9ca5-57be-432d-a920-ae168ef76ec5-cityPage%22}%2C%22sou%22:{%22actionid%22:%221bbef9c8-e7b2-4632-bbca-e5f9c836ab86-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%222ab4ed58-beb7-46eb-8d20-8695d0707e70-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_evtseq=83',
        'referer': 'https://www.zhaopin.com/beijing/',
    }

    def parse(self, response):  #parse解析    解析响应对象  在运行时会被引擎自动调用
        # response 是引擎直接返回的响应对象 是下载器间接返回的响应对象
        #response可以直接使用xpath语法,还可以使用选择器对象.
        jobList = response.xpath('//a[@class="zp-jobNavigater__pop--href"]/text()').extract()
        url = 'https://fecdn2.zhaopin.cn/www/citymap.web.2f8e0a.js'
        cityList = re.findall('code:"(.*?)"',requests.get(url=url).text)
        for city in cityList:
            for job in jobList:
                for page in range(0, 12):
                    url1='https://fe-api.zhaopin.com/c/i/sou?start={page}&pageSize=90&cityId={city}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={job}&kt=3&_v=0.47145290&x-zp-page-request-id=bd89c87aa13d4bf48c4d2c329eca145a-1563087529908-629530&x-zp-client-id=3f37f35c-eb68-4e6e-b6c2-74b7169cc215'.format(city=city, job=urllib.parse.quote(job), page=str(page*90))
        #     #发送一个请求(列表页) 发送请求 获取列表页html页面
                    yield scrapy.Request(url=url1,callback=self.parseList,headers=self.headers,dont_filter=True)   # dont_filter:是否不过滤
                    continue
    #     #解析列表页方法
    def parseList(self,response):   #启动任务:scrapy crawl zhilian33
        print('**************************************')
        restlt = response.text

        results_url=json.loads(restlt)['data']['results']

        # print(results_url)
        for i in results_url:
            print(i['positionURL']) #列表页url
            yield scrapy.Request(url=i['positionURL'],dont_filter=True,callback=self.detailParse,headers=self.headers)

    def detailParse(self,response): #解析详情页
        items=ZhilianItem(
        jobname=''.join(response.xpath('//h3[@class="summary-plane__title"]/text()').getall()),
        # print(jobname)
        salary=response.xpath('//span[@class="summary-plane__salary"]/text()').get(),
        # print(salary)
        city=response.xpath('//a[@href="//www.zhaopin.com/beijing/"]/text()').get(),
        # print(city)
        company=''.join(response.xpath('//*[@id="root"]/div[4]/div[2]/div[1]/div/a[1]/text()').getall()),
        # print(company)
        company_des=response.xpath('//div[@class="company__description"]/text()').get(),
        # print(company_des)
        job_des=response.xpath('string(//div[@class="describtion"])').get(),
        # print(job_des)
        )

        return items





# https://pypi.python.org/simple
# 错误:从命令python setup中完成输出。
# py egg_info错误:Traceback(最近一次调用last)。
# 文件“C: \ \用户本地管理员\ AppData \ \ Temp \ pip-install-neumvn73 \ pvecharts \设置。
# ，第8行，<module> from jupyterpip import cmdclass重要提示:没有名为jupyterpip的模块在处理上述异常期间，
# 发生了另一个异常回溯(最近一次调用last):文件“(string”，第1行，在<module中)文件C: \Users\Administrator\AppData\Local \Temp\pip-install-neumvn73 \pyecharts\setup。
# ， <module) pip中的第11行。
# (C' install'， ' jupyl -pip');cmdclass = importlib。
# 导入模块(“jupyterpip”)。
# cmdclass AttributeError:模块“pip”没有属性“main”错误:命令“pxthon setuo”。
# “py egg信息”在C语言中失败，错误代码1:用户管理员的AppDatal本地Templpip-install-neumvn73 pvecharts



