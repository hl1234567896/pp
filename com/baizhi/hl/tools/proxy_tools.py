import requests
from lxml import etree

def check(*args):
    try:
        r1=requests.get(url='http://www.httpbin.org/ip').text
        r2=requests.get(url='http://www.httpbin.org/ip',proxies={args[2]:args[0]+':'+args[1]}).text
        if r1==r2:  #表示不成功
            return False
        else:
            return True
    except:
        return False


def getOneProxy():
    targetUrl='https://www.kuaidaili.com/free/'

    res=requests.get(url=targetUrl)
    e=etree.HTML(res.text)
    trs=e.xpath('//tr')[1:]
    for tr in trs:
        ip,port,types=tr.xpath('./td[1]/text() | ./td[2]/text() | ./td[4]/text()')
        print(ip,port,types)
        if check(ip,port,types):
            return {types:ip+':'+port}
        # ip=tr.xpath('./td[1]/text()')
        # port=tr.xpath('./td[2]/text()')
        # types=tr.xpath('./td[4]/text()')
        # print(ip,port,types)



if __name__ == '__main__':
    getOneProxy()



















