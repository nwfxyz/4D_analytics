import requests
import json
from datetime import datetime
import pandas as pd
url = 'http://www.singaporepools.com.sg/_layouts/15/FourD/FourDCommon.aspx/Get4DNumberCheckResultsJSON'
headers = {
    'Host':'www.singaporepools.com.sg',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://www.singaporepools.com.sg/en/product/Pages/4d_cpwn.aspx',
    'Content-Type':'application/json',
    'X-Requested-With':'XMLHttpRequest',
    'Content-Length':'76'
}



def getDateFromDrawDate(x):
    x = x.replace('/Date(','')
    x = int(x.replace(')/',''))
    return datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d')


def GetResultsJson(num):
    data = json.dumps({"numbers":[str(num).zfill(4)], "checkCombinations":"true", "sortTypeInteger":"1"})
    r = requests.post(url=url, data=data, headers=headers)
    ResultsData = json.loads(r.json().get('d'))[0].get('Prizes')
    Results_df = pd.DataFrame.from_dict(ResultsData)
    Results_df["DrawDate"] = Results_df["DrawDate"].apply(getDateFromDrawDate,1)
    Results_df["Digit"] = str(num).zfill(4)
    return Results_df


ResultsAll = pd.DataFrame()
for i in range(0,10000):
    ResultsData = None
    while ResultsData is None:
        try:
            print(i)
            ResultsData = GetResultsJson(i)
        except:
            pass
    ResultsAll = ResultsAll.append(ResultsData)


ResultsAll.to_csv("Results.csv")
