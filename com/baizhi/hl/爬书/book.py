import requests,re
import MySQLdb
conn=MySQLdb.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='piaochong',
    charset='utf8'
)
cursor=conn.cursor()
'''
这两个网址没了
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.39.15ad5109hXDZPp&id=545031266275&rn=0fc04c4080582684bd50491e3f24c9d5&abbucket=18
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.42.15ad5109NoWEAD&id=556788253436&rn=12ea75dfab2145761a0802bfb4d6a0f7&abbucket=19
'''


aa='''
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.47.15ad5109HxzcLj&id=17115164231&rn=e1f17f959cbf6b65b420063b0933bfce&abbucket=19
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.63.15ad5109lu6g3a&id=16388545605&rn=91985d41b8f525a1182d8b99f75eb72e&abbucket=18
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.47.15ad5109lD0sHx&id=545021713847&rn=1d3f5e0e48759c309b2833efa5ff7810&abbucket=18
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.48.15ad5109jVJfOc&id=37278891640&rn=f58410985d0900e95ce06488c1eb22b5&abbucket=18
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-14990548188.46.4f7b2bc68aRWXb&id=527225491591&rn=fb4ab466ce073d5759ba0366a370f256&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.47.15ad5109BUVzk5&id=23013004554&rn=8acf636c29b44348551260feb1592ca9&abbucket=18
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.32.15ad5109fhIYwg&id=548375888584&rn=50915d0550eec11657cee653c7618dd4&abbucket=18
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.37.15ad5109QSXy5X&id=554029006056&rn=59c933bc9c1c1f4174c2a252d8e82eb9&abbucket=18
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.51.15ad5109oltrnX&id=17112472802&rn=75e0606ce4f2fa0ab5da95724e85825f&abbucket=5
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.37.15ad5109v014ce&id=547465419456&rn=c113d935cf06c1dd90b354ba0205dfcc&abbucket=5
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.38.15ad5109dQWzJh&id=542610801750&rn=0162394b989726b7d419c5bac784738a&abbucket=5


https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.44.3dc5132aWSBcvb&id=546486479789&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.50.3dc5132aWSBcvb&id=557418956215&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.65.3dc5132aWSBcvb&id=548478894879&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.56.3dc5132aWSBcvb&id=556459453356&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.53.3dc5132aWSBcvb&id=546464938988&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.77.3dc5132aWSBcvb&id=546487919080&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.89.3dc5132aWSBcvb&id=571290664306&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16167622159.47.3dc5132aWSBcvb&id=546517767438&rn=4b314df098d39e4dc68ed4cb463fc5b7&abbucket=10


https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16051564354.56.504b617c5tYMuj&id=545778336090&rn=7882c9655d6aeee95ab70d2477d15d86&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16051564354.78.504b617c5tYMuj&id=578937285658&rn=7882c9655d6aeee95ab70d2477d15d86&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16051564354.48.504b617c5tYMuj&id=545799408189&rn=7882c9655d6aeee95ab70d2477d15d86&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16051564354.62.504b617c5tYMuj&id=545841711769&rn=7882c9655d6aeee95ab70d2477d15d86&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16051564354.60.504b617c5tYMuj&id=575309488287&rn=7882c9655d6aeee95ab70d2477d15d86&abbucket=10
https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16051564354.54.504b617c5tYMuj&id=545799776744&rn=7882c9655d6aeee95ab70d2477d15d86&abbucket=10


'''
headers={
    'cookie':'cna=IBSfFTg3MBgCAXWIJoRddSuA; t=057d82f7c3ed85df244fe41492a7e299; _tb_token_=e431e16373f43; cookie2=109ba7e57a5c5afa5e9ef9d15da9f39a; hng=""; tracknick=t_1489244718861_0104; ck1=""; lgc=t_1489244718861_0104; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=61023; x=__ll%3D-1%26_ato%3D0; skt=992c4225b62e8e74; dnk=t_1489244718861_0104; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTaG7u%2FYrmcqw%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dBy3zdlkw7aMxglnw%3D&id2=UUpkvTD43a9%2B9A%3D%3D&nk2=F6k3HMozSd5Vy1%2BBRFVM%2FeAUZxo%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lid=t_1489244718861_0104; _l_g_=Ug%3D%3D; unb=2255386203; cookie1=BxNTFJ0%2FAWy4g%2BUETbbj8KAPrOciVFgPHnQiMbbR21M%3D; login=true; cookie17=UUpkvTD43a9%2B9A%3D%3D; _nk_=t_1489244718861_0104; sg=433; csg=6ffb21c2; enc=OFd%2BlyHxJx0FVfyx8VJYGfqI4P%2FkkmuOLoQXhCNDpH81UPQLx2B9Vi463WXKASrLeaYhc15Uh3szVsDN1ob6oQ%3D%3D; cq=ccp%3D0; _m_h5_tk=fad7cdd15e75af32e78705218eb84a83_1563452595515; _m_h5_tk_enc=8c8f4b181304a0fabd12a51fa2dd4182; pnm_cku822=098%23E1hvRQvUvbpvUvCkvvvvvjiPRFMp6j3RP25v6jivPmPptjDCnLzy6jrWRs59QjYRiQhvCvvvpZptvpvhvvCvpbyCvm9vvhCvvvvvvvvvByOvvvHMvvCVB9vv9LvvvhXVvvmCI9vvByOvvUVkkphvC9hvpyPwl8yCvv9vvhhrhvUcVpyCvhQCcrbojwVTKLpZEcqpaXp7%2Bul68NoxdBkKjztP0bmAdBKKNZMUgE7AdX%2BaWXxr58TJ%2B3%2BSaXkAdBKKfvDrl8gcRbIs7TmxdXAKDVQEvphvC9mvphvvvvGCvvpvvPMM; whl=-1%260%260%260; l=cBjlJwSVqSxdA6-DKOCwlurza77tRIRAguPzaNbMi_5KF1Y6Ar_OkqUjEev6cjWdOvLp45fyK2e9-etksMjBXxCP97RN.; isg=BJGRxRRVqJBeuMSacu6TgACFoJ0r_gVwmb8Vn3Mmpdh3GrFsuky_QD9wvK5ZEp2o',
    'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15421479640.47.15ad5109HxzcLj&id=17115164231&rn=e1f17f959cbf6b65b420063b0933bfce&abbucket=19',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

all_list=re.findall('id=(.*?)&', aa)
try:
    for i in all_list:
        url='https://mdskip.taobao.com/core/initItemDetail.htm?itemId='+i
        res=requests.get(url=url,headers=headers)
        saleprice=re.findall('"price":"(.*?)"',res.text)[-1]
        print(saleprice)
        cursor.execute("update book_details set saleprice={} where url like '%{}%'".format(saleprice,i))
        conn.commit()
finally:
    print('关闭资源')
    cursor.close()
    conn.close()







