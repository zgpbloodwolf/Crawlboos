import requests
from collections import deque
import json
url = "https://www.zhipin.com/wapi/zpCommon/data/position.json"
r = requests.get(url)
zplist = r.json()['zpData']
majorlist=[]
major={}
def center(adlist):
    que = deque()
    que.append(adlist)
    while len(que) !=0:
        try:
            addli = que.popleft()
            for i in addli:
                if i['subLevelModelList']:
                    que.append(i['subLevelModelList'])
                else:
                    majorlist.append(i["code"])
        except :
            pass
center(zplist)
major["major"]=majorlist
with open('major.json','w') as f:
    f.write(json.dumps(major,ensure_ascii=False))

