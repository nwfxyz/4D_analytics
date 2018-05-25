import requests
import json
from itertools import combinations_with_replacement
import time

def generate_4d():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    unique = ["".join(map(str, comb)) for comb in combinations_with_replacement(numbers, 4)]
    return unique

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

numbers = generate_4d()
errors = []

for number in numbers:
    data = json.dumps({"numbers":['{}'.format(number), ""], "checkCombinations":"true", "sortTypeInteger":"1"})
    print(data)
    r = requests.post(url=url, data=data, headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        result = json.loads(r.text)
        prizes = json.loads(result['d'])
        print(prizes)
        with open('4drawresults.json', 'a+', encoding='utf-8') as f:
            json.dump(prizes[0], f, indent=4)
            f.write('\n')
    else:
        print(r.status_code)
        errors.append(number)
    time.sleep(1)

with open('errors.txt', 'w+', encoding='utf-8') as f:
    for item in errors:
        f.write("{}\n".format(item))
