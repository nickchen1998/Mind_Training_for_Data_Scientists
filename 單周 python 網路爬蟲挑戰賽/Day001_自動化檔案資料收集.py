# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 05:00:01 2021

@author: nick
"""

import urllib.request
import csv
from pprint import pprint

url = "https://data.nhi.gov.tw/resource/mask/maskdata.csv"
urllib.request.urlretrieve(url, './maskdata.csv')

data_dict = {}

with open("./maskdata.csv", "r", encoding="utf8") as csvfile:
    datas = csv.reader(csvfile)
    next(datas) # remove header
    
    for rows in datas:
        if rows[2][:3] not in data_dict:
            data_dict[rows[2][:3]] = {"成人口罩剩餘數": int(rows[4]), "兒童口罩剩餘數":int(rows[5])}
        
        # 如果該縣市已經在字典內，則直接調出上一家藥局的剩餘數量進行加總
        elif rows[2][:3] in data_dict:
            data_dict[rows[2][:3]]["成人口罩剩餘數"] += int(rows[4])
            data_dict[rows[2][:3]]["兒童口罩剩餘數"] += int(rows[5])
            
pprint(data_dict) # pprint 用於美化輸出，不介意看擠在一起的東西的話可以直接用 print()
