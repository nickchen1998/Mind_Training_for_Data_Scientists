# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:28:37 2021

@author: nick
"""

import requests, json, time
import pandas as pd

key = ""
city = "Taipei"
api = "https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={key}".format(city=city, key=key)

data = requests.get(api)
result = json.loads(data.text)["list"]

result_lst = []

for item in result:
    result_lst.append([])
    result_lst[len(result_lst)-1].append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(item['dt'])))) # 加入預測時間
    result_lst[len(result_lst)-1].append(item['main']['temp']) # 加入預測溫度
    result_lst[len(result_lst)-1].append(item['main']['feels_like']) # 加入體感溫度
    result_lst[len(result_lst)-1].append(item['main']['temp_min']) # 加入預測最小溫度
    result_lst[len(result_lst)-1].append(item['main']['temp_max']) # 加入預測最大溫度

columns = ["預測時間", "預測溫度", "預測體感溫度", "預測最小溫度", "預測最大溫度"]


df = pd.DataFrame(result_lst, columns=columns)
sort_df = df.sort_values(by="預測溫度", ascending=False)
print(sort_df.head(1))

