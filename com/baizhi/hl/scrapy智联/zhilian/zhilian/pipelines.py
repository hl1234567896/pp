# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class ZhilianPipeline(object):
    def __init__(self,host,port,user,password,db,charset):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset

    def process_item(self, item, spider):
        print('************************入库思密达************************')

        self.cursor.execute(self.sql,(item['jobname'],item['salary'],item['city'],item['company'],item['company_des'],item['job_des'],))
        self.conn.commit()

    def open_spider(self,spider):   #数据库初始化 当爬虫开启时自动调用
        self.conn=MySQLdb.Connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  db=self.db,
                                  charset=self.charset,
                                  )
        self.cursor=self.conn.cursor()
        self.sql='insert into zhilian_scrapy values ("%s","%s","%s","%s","%s","%s")'

    def close_spider(self,spider):  #当spider关闭时自动调用
        self.cursor.close()
        self.conn.close()

    # 该方法用于创建pipeline对象
    @classmethod
    def from_crawler(cls,crawler):  #是一个类方法
        # host=crawler.settings.get('HOST','localhost'),
        # port=crawler.settings.get('PORT',3306),
        # user=crawler.settings.get('USER','root'),
        # password=crawler.settings.get('PASSWORD','123456'),
        # db=crawler.settings.get('DB','piaochong'),
        # charset=crawler.settings.get('CHARSET','utf8')
        host = 'localhost'
        port = 3306
        user =  'root'
        password = '123456'
        db =  'piaochong'
        charset =  'utf8'
        print(host)
        print(port)
        print(user)
        print(password)
        print(db)
        print(charset)
        try:
            MySQLdb.Connect(host=host,port=port,user=user,password=password,db=db,charset=charset)
            return cls(host=host,port=port,user=user,password=password,db=db,charset=charset)
        except:
            print(11111)
            return None

#去重
from scrapy.exceptions import DropItem
class DropPipeline: #去重
    def __init__(self):
        self.temp = set()  # 设置空集合
    def process_item(self,item,spider):
        if not item['jobname']:
            item['jobname']=''
        if not item['company']:
            item['company']=''
        data=item['jobname']+item['company']
        if data in self.temp:   #如果有重复
            return DropItem('这个重复')
        else:
            self.temp.add(data)
            return item

#q清洗
# import re
# r=re.compile('\S*')
# import jieba
# import jieba.analyse as ja
# class CleanPipeLine:
#     def process_item(self,item,spider):
#         item['job_des']=''.join(r.findall(item['job_des'])) #去除不要的字符串
#         item['job_des']='/'.join(ja.extract_tags(item['job_des'],topK=30))  #提取关键字
#         if item['job_des']=='':
#             item['job_des']='无'









