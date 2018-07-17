#爬去王者荣耀官网皮肤图片
#background: http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/503/503-bigskin-2.jpg
import requests
import json
import  urllib
with open('D:\\python\\King\\venv\\herolist.json','r',encoding='utf-8') as ff:
    jsonFile=json.load(ff)
for i in range(len(jsonFile)):
    #英雄编号
    eName=jsonFile[i]['ename']
    #英雄名字
    cName=jsonFile[i]['cname']
    title=jsonFile[i]['title']
    skinName=jsonFile[i]['skin_name']
    skinName=skinName.split("|")
    #皮肤数量
    skin_numbers=len(skinName)
    for j in range(1,skin_numbers+1):
        #print(pictureUrl)
        pictureUrl='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(eName)+'/'+str(eName)+'-bigskin-'+str(j)+'.jpg'
        '''
        第一种方法
        picture=requests.request('get',pictureUrl).content
        with open('C:\\Users\\zhuangwei\\Desktop\\King\\'+cName+skinName[j-1]+'.jpg','wb')as ff:
            ff.write(picture)
        '''
        #第二种方法
        urllib.request.urlretrieve(pictureUrl,'C:\\Users\\zhuangwei\\Desktop\\King\\'+cName+skinName[j-1]+'.jpg')