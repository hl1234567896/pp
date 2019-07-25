from lxml import etree
import requests

url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.92122073&x-zp-page-request-id=0040d0e6ef0a4510bcac4e595ceddeee-1562636783604-3930&x-zp-client-id=3f37f35c-eb68-4e6e-b6c2-74b7169cc215'

# res=requests.get(url=url)
# data1=res.json()['data']['results']
# for i in data1:
#     result=requests.get(url=i['positionURL'])
#     e=etree.HTML(result.text)
#     print(e.xpath('//h3[@class="summary-plane__title"]/text()'))


with requests.session() as s:
    res=s.get(url=url)
    data1=res.json()['data']['results']
    for i in data1:
        result=requests.get(url=i['positionURL'])
        e=etree.HTML(result.text)
        print(e.xpath('//h3[@class="summary-plane__title"]/text()'))







