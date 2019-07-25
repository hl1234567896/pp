import MySQLdb
import re
import urllib.request as ur

conn = MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		    # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="day01",          # 要使用的库名
    charset="utf8"      # 连接中使用的字符集
)
cursor = conn.cursor()  # 游标

'''
<a href="https://jobs.zhaopin.com/CC333330380J00059929313.htm" zp-stat-jdno="CC333330380J00059929313" zp-stat-pos="0" zp-stat-pageno="1" zp-stat-pagelim="90" zp-stat-funczone="401901" target="_blank" zp-stat-track="jd_click" zp-stat-id="jd_click" class="contentpile__content__wrapper__item__info"><div class="contentpile__content__wrapper__item__info__box
                  contentpile__content__wrapper__item__info__box--name itemBox nameBox"><div class="contentpile__content__wrapper__item__info__box__jobname jobName"><span title="后端开发工程师（python、go）" class="contentpile__content__wrapper__item__info__box__jobname__title">后端开发工程师（<span style="color: #FF5959;">python</span>、go）</span> <!----> <!----> <!----> <!----> <!----></div> <div class="contentpile__content__wrapper__item__info__box__cname
                  commpanyName"><img src="//img03.zhaopin.cn/IHRNB/img/detailviph.png" alt="观止云(北京)信息技术有限公司" title="观止云(北京)信息技术有限公司" class="contentpile__content__wrapper__item__info__box__cname__viplevel is_vipLevel"> <a href="https://company.zhaopin.com/CZ333330380.htm" title="观止云(北京)信息技术有限公司" target="_blank" class="contentpile__content__wrapper__item__info__box__cname__title company_title">观止云(北京)信息技术有限公司</a></div></div> <div class="contentpile__content__wrapper__item__info__box
              contentpile__content__wrapper__item__info--desc itemBox descBox"><div class="contentpile__content__wrapper__item__info__box__job jobDesc"><p class="contentpile__content__wrapper__item__info__box__job__saray">12K-18K</p> <ul class="contentpile__content__wrapper__item__info__box__job__demand"><li class="contentpile__content__wrapper__item__info__box__job__demand__item">北京</li> <li class="contentpile__content__wrapper__item__info__box__job__demand__item">
                    3-5年
                  </li> <li class="contentpile__content__wrapper__item__info__box__job__demand__item">本科</li></ul></div> <div class="contentpile__content__wrapper__item__info__box__job__comdec"><span class="contentpile__content__wrapper__item__info__box__job__comdec__item">民营 </span> <span class="contentpile__content__wrapper__item__info__box__job__comdec__item">20-99人 </span></div></div> <div class="contentpile__content__wrapper__item__info__box itemBox"><div class="contentpile__content__wrapper__item__info__box__welfare job_welfare"><div class="contentpile__content__wrapper__item__info__box__welfare__item
                   contentpile__content__wrapper__eager-talents">求贤若渴</div> <div class="contentpile__content__wrapper__item__info__box__welfare__item">五险一金</div><div class="contentpile__content__wrapper__item__info__box__welfare__item">绩效奖金</div><div class="contentpile__content__wrapper__item__info__box__welfare__item">全勤奖</div><div class="contentpile__content__wrapper__item__info__box__welfare__item">餐补</div><div class="contentpile__content__wrapper__item__info__box__welfare__item">通讯补助</div></div> <div class="contentpile__content__wrapper__item__info__box__status"><span class="contentpile__content__wrapper__item__info__box__status__recruit">最新</span> <!----></div></div></a>
zp-stat-jdno
'''

url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.13780778&x-zp-page-request-id=5d8f378066d74494ac1ed4b9a447f7ff-1561994502575-687815&x-zp-client-id=3f37f35c-eb68-4e6e-b6c2-74b7169cc215'
res=ur.urlopen(url=url)
res1=res.read().decode('utf-8')
# print(res1)
rule='"https://jobs.zhaopin.com/.*?"'
urllist=re.findall(rule,res1)   #第一页所有链接
for i in urllist:
    i_url=i[1:][:-1]
    print(i_url)








































