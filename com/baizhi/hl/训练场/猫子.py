import  requests
from lxml import etree
import MySQLdb

class CrawlerTools: #工具类 供别人使用  可扩展性
    def __init__(self,start_url):   #1.创建对象时自动调用 2.让机制自动发送一次请求
        self.start_url = start_url
        self.element = etree.HTML(requests.get(url=self.start_url).text)#起始列表页的element对象
        self.nextpageLink = self.start_url

    def getpageList(self,url=''):   #获取列表页
        url = self.start_url if not url else url
        res = requests.get(url=url)
        e = etree.HTML(res.text)    #构建列表页的element对象
        detailpageList = e.xpath('//a[@class="image-link"]/@href')
        detailpageList = ['https://maoyan.com'+ i for i in detailpageList]
        return detailpageList

    def parsePage(self,detail_url): #解析详情页
        res = requests.get(url=detail_url)  #访问详情页
        e = etree.HTML(res.text)
        nameList = e.xpath('string(//div[@class="movie-brief-container"])')
        desc = e.xpath('//span[@class="dra"]//text()')
        return ''.join([i for i in nameList if i!=' ']).replace('\n','/'),desc    #返回的是一个数据,系统会自动打包成元组返回

    def nextpage(self):
        nextButton = etree.HTML(requests.get(url=self.nextpageLink).text).xpath('//ul[@class="list-pager"]//a')
        for i in nextButton:
            if i.xpath('./text()')[0] =='下一页':
                newpage = 'https://maoyan.com/board/4'+i.xpath('./@href')[0]
                self.nextpageLink = newpage
                yield self.getpageList(self.nextpageLink)
        return None


class DBTools:
    def __init__(self):
        # 创建链接
        self.conn=MySQLdb.Connect(host='localhost',user='root',password='123456',port=3306,db='piaochong',charset='utf8')
        # 创建游标
        self.cursor=self.conn.cursor()
        # 创建sql
        self.sql='insert into maozi values(%s,%s)'

    def add(self,*args):
        # 执行sql
        self.cursor.execute(self.sql,args)
        self.conn.commit()

    # 关闭资源
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
     tools = CrawlerTools('https://maoyan.com/board/4?offset=0')
     dbTools = DBTools()
     for i in tools.getpageList():
         dbTools.add(*tools.parsePage(i))
     for i in tools.getpageList():
         for k in tools.nextpage():
             for j in k:
                 dbTools.add(*tools.parsePage(j))
     dbTools.close()

