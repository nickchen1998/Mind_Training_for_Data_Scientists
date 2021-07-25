# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:01:11 2021

@author: nick
"""
import requests, json
import pandas as pd

# 取得資料
url = 'https://www.dcard.tw/_api/forums'
datas = requests.get(url)
result = json.loads(datas.text)

# 建立空串列存放資料
result_lst = []

# 利用 for 逐一走訪資料並存入 list
for item in result:
    result_lst.append([])
    result_lst[len(result_lst)-1].append(item['name'])
    result_lst[len(result_lst)-1].append(item['subscriptionCount'])

# 建立 DataFrame 的標頭以及 DataFrame
columns = ["看板名稱", "訂閱人數"]
df = pd.DataFrame(result_lst, columns=columns)

# 利用 "訂閱人數" 進行排序，並且印出前五筆資料即可
print(df.sort_values(by="訂閱人數", ascending=False).head(5))