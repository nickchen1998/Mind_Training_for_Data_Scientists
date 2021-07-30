# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:36:10 2021

@author: nick
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup as soup

res = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html", cookies={"over18":"1"})

datas = soup(res.text, "lxml").find_all("div", class_="r-ent")

result = []

for item in datas:
    result.append([])
    result[len(result)-1].append(item.find("div", class_="title").text.replace("\n", ""))
    result[len(result)-1].append(item.find("div", class_="date").text)
    
columns = ["標題", "發文時間"]
df = pd.DataFrame(result, columns=columns)

print(df)