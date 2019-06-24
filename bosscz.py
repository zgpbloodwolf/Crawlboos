import requests
import json
url = "https://www.zhipin.com/wapi/zpCommon/data/city.json"
r = requests.get(url)
zplist = r.json()["zpData"]
addlist=[]
address={}
for i in ['cityList','hotCityList']:
    print(i)
    for j in zplist[i]:
        if j['subLevelModelList']:
            for k in j['subLevelModelList']:
                addlist.append(k["code"])
        else:
           addlist.append(j['code'])
addlist=list(set(addlist))
address['address']=addlist
with open('address.json','w') as f:
    f.write(json.dumps(address,ensure_ascii=False))

