# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

# class JobPipeline(object):  #千万要注意 记得在settings.py文件中进行设置
#     def process_item(self, item, spider):
#         print('*************************************************')
#         #入库
#         conn=MySQLdb.Connect(
#             host='localhost',
#             port =3306,
#             user='root',
#             password='123456',
#             db='piaochong',
#             charset='utf8',
#         )
#         cursor=conn.cursor()
#         sql='insert into job51 values ("%s","%s","%s","%s","%s")'
#         cursor.execute(sql,(item['job_name'],item['job_message'],item['company_name'],item['company_information'],item['good']))
#         conn.commit()
#         cursor.close()
#         conn.close()

# import MySQLdb    #51job
# class JobPipeline(object):
#     def __init__(self):
#         self.conn = MySQLdb.Connect(host='localhost',
#                                     port=3306,
#                                     user='root',
#                                     password='123456',
#                                     db='piaochong',
#                                     charset='utf8',
#                                     )
#         self.cursor = self.conn.cursor()
#         self.sql = 'insert into job52 values("%s","%s","%s","%s","%s")'
#     def process_item(self, item, spider):
#         # print('****************************')
#         # 入库
#         self.cursor.execute(self.sql, (item['job_name'], item['job_message'],item['company_name'],item['company_information'],item['good']))
#         self.conn.commit()



#新来的
class JobPipeline(object):
    def __init__(self,host,port,user,password,db,charset):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset


    def process_item(self,item,spider): #入库
        print('**********************************************************')

        self.cursor.excute(self.sql,(item['job_name'], item['job_message'],item['company_name'],item['company_information'],item['good']))
        self.conn.commit()


    def open_spider(self,spider):   #当爬虫开启的时候自动调用该方法
        #数据库初始化
        self.conn = MySQLdb.Connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset,
                                    )
        self.cursor=self.conn.cursor()
        self.sql='insert into job52 values ("%s","%s","%s","%s","%s")'


    def close_spider(self,spider):  #当spider关闭时自动调用
        self.cursor.close()
        self.conn.close()


    @classmethod
    def from_crawler(cls,crawler):  #是一个类方法 容错率高
        host = crawler.settings.get('HOST', 'localhost'),
        port = crawler.settings.get('PORT', 3306),
        user = crawler.settings.get('USER', 'root'),
        password = crawler.settings.get('PASSWORD', '123456'),
        db = crawler.settings.get('DB', 'piaochong'),
        charset = crawler.settings.get('CHARSET', 'utf8')
        try:
            MySQLdb.Connect(host=host,port=port,user=user,password=password,db=db,charset=charset)
            return cls(host=host,port=port,user=user,password=password,db=db,charset=charset)
        except:
            return None

from scrapy.exceptions import DropItem
# 去重
class DropPipeline:
    def __init__(self):
        self.temp=set()  #设置空集合
    def process_item(self,item,spider): #去重? 集合
        data=item['job_name']+item['job_message']
        if data in self.temp:   #重复了
            return DropItem('该item已经存在')
        else:   #没重复
            self.temp.add(item) #加进去
            return item
#
#
#清洗
class CleanPipelinne:
    def process_item(self,item,spider):
        pass









