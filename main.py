from fastapi import FastAPI
import requests

def get_tastedive(movieName, limit=5, key="410571-StudyApl-KT62OLS2"):
    baseurl="https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"]= movieName
    params_d["k"]= key
    params_d["type"]= "movies"
    params_d["limit"] = limit
    resp = requests.get(baseurl, params=params_d)
    # print(resp.url)
    respDic = resp.json()
    return respDic 

app = FastAPI()

@app.get('/{name}/{limit}')
def home(name: str, limit: int):
    dict = get_tastedive(name, limit)['Similar']['Results']
    #print(dict.values)
    list = [x['Name'] for x in dict ]
    return list