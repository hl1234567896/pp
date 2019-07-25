'''
IP代理池:
数据库:存ip 端口号 类型 proxy_pool
架构: 类 提供IP:工具
编码:

功能:
1.给用户提供代理
2.检测IP是否可用
3.爬取IP
4.保存到数据库
5.检测代理池有多少可用的IP
6.检测是否需要补充IP
'''

import MySQLdb
from lxml import etree
import requests

class PorxyPool(object):
    #属性
    #测试网站URL
    TEST_URL = 'http://www.httpbin.org/ip'
    #方法 普通方法 初始化方法
    def __init__(self,limit=3,volume=10,tartgetURL='https://www.kuaidaili.com/free/'):
        self.targetURL=tartgetURL   #目标网站URL(提供IP)
        self.dbInit()   #数据库
        self.limit=limit    #阈值
        self.pageNum=1  #设置初始页码
        self.volume=volume  #设置容量
        self.response=requests.get(url=self.TEST_URL).text


    def dbInit(self):   #创建链接
        self.conn=MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='piaochong',
            charset='utf8'
        )

        self.cursor=self.conn.cursor()  #创建游标


    def getOneIP(self): #爬取IP
        while 1:
            res=requests.get(self.targetURL+str(self.pageNum))  #url拼接码
            self.pageNum+=1
            if self.pageNum>2500:
                self.pageNum=1
            e=etree.HTML(res.text)
            #获取tr标签
            trs=e.xpath('//tr[@class="odd"]')   #列表
            for tr in trs:
                ip=tr.xpath('//td[2]/text()')
                port=tr.xpath('//td[3]/text()')
                types=tr.xpath('//td[6]/text()')

                if self.checkIP(ip,port,types): #测试 可用就入库
                    self.cursor.execute('insert into xici values(%s,%s,%s,1)',(ip,port,types))
                else:
                    pass

            if self.getAllProxyAvailable()==self.volume:    #爬取的数量=阈值时,停止
                break

    def checkIP(self,ip,port,types):    #检查是否可用
        try:
            response=requests.get(url=self.TEST_URL,proxies={types:ip+':'+port}).text
            if self.response==response:     #表示不可用
                return False
            else:
                return True
        except:
            return False    #没网或者IP被封也是False

    def getAllProxyAvailable(self): #获得所有可用的IP数量
        self.cursor.execute('select count(*) from xici where status=1') #查看所有状态为1的数据
        resultNumber=self.cursor.fetchone()[0]  #cursor.fetchone()       #在查询出的数据中，获取一条数据
        return resultNumber

    def api(self):  #给用户提供IP
        self.cursor.execute('select ip,port,types from xici where status=1 limit 1')  #从数据库取出一个可用IP并返回
        result=self.cursor.fetchone()   #(ip,port,types)
        self.cursor.execute('update xici set status=0 where ip=%s',result[0])   #将本数据修改状态
        self.conn.commit()
        self.appendProxy()  #判断你是否达到阈值,并进行补充
        return result

    def appendProxy(self):  #判断阈值,补充数据
        if self.getAllProxyAvailable()<self.limit:
            self.getOneIP() #进行补充,爬取数据

    def checkRegular(self): #一定要使用多线程
        from apscheduler.schedulers.blocking import BlockingScheduler   #定时
        sch=BlockingScheduler()
        def fun():
            self.cursor.execute('select ip,port,types from xici')
            for i in self.cursor.fetchall():    #i每条数据
                if self.checkIP(i): #检查是否可用
                    self.cursor.execute('update xici set status=1 where ip=%s',i[0])
                else:
                    self.cursor.execute('update xici set status=0 where ip=%s',i[0])

                self.conn.commit()
            self.appendProxy()
        sch.add_job(fun,'cron',second='*/600')
        sch.start()



if __name__ == '__main__':  #
    import threading
    pp=PorxyPool()
    threading.Thread(target=pp.checkRegular(),daemon=True).start()























