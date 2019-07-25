

import requests
from lxml import etree

url='https://maoyan.com/board/4'
res=requests.get(url=url)   # 获得一个response对象
e=etree.HTML(res.text)  # 将text转换为element对象

#处理一页数据
def onePageHandler(e):
    #使用xpath解析每一个详情页的连接
    detailList=e.xpath('//a[@class="image-link"]/@href')    #详情页列表
    detailList=['https://maoyan.com'+i for i in detailList]
    return detailList

#处理详情页数据
def detailPageHandler(e,path='https://maoyan.com/board/4'):    #是一个生成器---按需供应
#处理分页
    r1=e.xpath('//ul[@class="list-pager"]/li[9]/@href')     #每个下一页链接
    for i in r1:
        yield  path + i

    # nextPageLink=['https://maoyan.com/board/4'+i for i in r1]   #补全所有的下一页链接

    # temp=[requests.get(url=i)for i in nextPageLink] #访问下一页链接    2-10页的所有页面的链接



def main():
    #调用第一页
    firstPageList=onePageHandler(e)
    twoToTenPageLink=detailPageHandler(e)
    #进入第一页每一个详情
    #访问第二页之后的下一页链接
    #进入下一页的每一个详情


# if __name__ == '__main__':