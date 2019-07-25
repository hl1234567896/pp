# import requests
# from lxml import etree
#
# url='http://www.hanjutv.com/top/tv/'
# res=requests.get(url=url)
# ele=etree.HTML(res.text)
# all_video_links=ele.xpath('//li[@class="item_list"]/span/a/@href')
# video_link='http://www.hanjutv.com'+all_video_links[0]
#
# print('进入一个傻逼韩剧',video_link)
# headers={
#     'Cookie':'__cfduid=df7cd7c582242daaee00cdef2faaad2d71563362952; UM_distinctid=16bffb1727c68-073e5ac19b02c1-404b032d-144000-16bffb1727d53a; poscms_ci_session=86ut3lfah8pj9ont401831omkialpbbk; _widget_vip=0; Hm_lvt_06d18bf0dcdca7a8e084a650d5e8b245=1563362965,1563363538,1563365626; CNZZDATA1277228780=1167097352-1563361579-https%253A%252F%252Fwww.baidu.com%252F%7C1563366979; CNZZDATA1257743765=1868461450-1563362141-https%253A%252F%252Fwww.baidu.com%252F%7C1563367543; Hm_lpvt_06d18bf0dcdca7a8e084a650d5e8b245=1563367677',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#     'Referer':'http://www.hanjutv.com/top/tv/'
# }
# res1=requests.get(url=video_link,headers=headers)
# ele1=etree.HTML(res.text)
# print(ele1)
# video=ele1.xpath('//ul[@class="juji-list clearfix"]/li/a/@href')
# print(video)

# import os
# # url='https://www.bilibili.com/video/av46024782?from=search&seid=11715108094899958189'
# url='http://www.hanjutv.com/player/35258.html'
# path='G:\课程\第三阶段\you-get下载视频'
# os.system('you-get -o {path} {url}'.format(path=path,url=url))



























