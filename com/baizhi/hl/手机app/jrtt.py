import requests
from lxml import etree


# url='http://ic.snssdk.com/api/news/feed/v88/?list_count=10&refer=1&iid=78394927227&device_id=62723135700&ac=wifi&channel=baidu&aid=13&app_name=news_article&version_code=727&version_name=7.2.7&device_platform=android&ab_version=665173%2C674055%2C964118%2C643894%2C1002926%2C649429%2C677128%2C710077%2C801968%2C707372%2C1001980%2C661905%2C668775%2C982553%2C971380%2C739393%2C662099%2C668774%2C765195%2C976875%2C857804%2C952274%2C757283%2C679101%2C660830%2C830855%2C814658%2C991360%2C662176%2C759655%2C661781&ab_feature=102749%2C94563&ssmix=a&device_type=SM-G955F&device_brand=samsung&language=zh&os_api=22&os_version=5.1.1&uuid=355757010164024&openudid=a402b95fccf62982&manifest_version_code=727&resolution=1280*720&dpi=240&update_version_code=72711&_rticket=1562835932736&plugin=0&fp=R2TZFrPMLSL_Flw7cSU1FzFWLlw7&pos=5r_-9Onkv6e_v7G_8fLz-vTp6Pn4v6esraqzqKuuqKWsq6urq6urq6ixv_H86fTp6Pn4v6euq7OtrayvqOA%3D&rom_version=22&ts=1562835932&as=a2f5afa27c9dcd5b768600&mas=007e807efae5261cca26842e2dbd65a1708480aad2a5c2c4e9'
#
# res=requests.get(url=url)
# data=res.json()
# print(data['data'][0]['content'])

url1='http://v3-dy-z.bytecdn.cn/d332c456cb78ca10bc8f85523eb2e1ea/5d2742f1/video/m/22067fbbbba71434354a6b6f9f88cc22b781162566f800000fff61b26fe0/?rc=M2h5ZWxrZTc5bTMzZ2kzM0ApQHRAbzU6ODUzNjg0NDs7NDQ6PDNAKXUpQGczdSlAZjV2KUBmcHcxZnNoaGRmOzRAcjFkci8yM2BtXy0tXy0wc3M1byNvI0A2NTAtLTItLTAtLy4tLi9pOmIwcCM6YS1xIzpgMG8jYmZoXitqdDojLy5e'
url2='http://v3-dy-x.bytecdn.cn/d0d0fcb38c7d990f5d86ee8cae1446c1/5d274670/video/m/220176b0278236b495da18b1c704ee196dc1162c7ab10000b471fe70926f/?rc=M2dpdmRrcGpqbjMzNWkzM0ApQHRAbzREOTozOTszNDU2NDQ6PDNAKXUpQGczdSlAZjV2KUBmcHcxZnNoaGRmOzRAb2QvbWMuY2FlXy0tLS0vc3M1byNvIy0tMzQvLS0tLTAvLy4tLi9pOmIwcCM6YS1xIzpgMG8jYmZoXitqdDojLy5e'
res=requests.get(url=url1)
print(res.content)


















