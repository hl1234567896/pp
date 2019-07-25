# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class ShangbiaoPipeline(object):
    def __init__(self,host,port,user,password,db,charset):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset


    def process_item(self, item, spider):
        # print('**********************入库思密达***********************')
        self.cursor.execute(self.sql,(item['num'],item['name']))
        self.conn.commit()
        return item

    def open_spider(self,spider):
        self.conn = MySQLdb.Connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset,
                                    )
        self.cursor = self.conn.cursor()
        self.sql='insert into shangbiao values ("%s","%s")'

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

    @classmethod
    def from_crawler(cls, spider):  # 是一个类方法
        # host=spider.settings.get('HOST','localhost'),
        # port=spider.settings.get('PORT',3306),
        # user=spider.settings.get('USER','root'),
        # password=spider.settings.get('PASSWORD','123456'),
        # db=spider.settings.get('DB','piaochong'),
        # charset=spider.settings.get('CHARSET','utf8')
        host = 'localhost'
        port = 3306
        user = 'root'
        password = '123456'
        db = 'piaochong'
        charset = 'utf8'
        # print(host)
        # print(port)
        # print(user)
        # print(password)
        # print(db)
        # print(charset)
        try:
            MySQLdb.Connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
            return cls(host=host, port=port, user=user, password=password, db=db, charset=charset)
        except:
            return None