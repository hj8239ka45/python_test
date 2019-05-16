import json
from requests import get

firebase_url = 'https://smartmanu-af015.firebaseio.com/.json'
data = get(firebase_url).json()['AGV']
state = []
mechine = ['CMM','EDM','HSM','Laser','WEDM']
for i in range(0,len(mechine)):
    state.append(data[mechine[i]])
print(state)#取得各個機台資料
