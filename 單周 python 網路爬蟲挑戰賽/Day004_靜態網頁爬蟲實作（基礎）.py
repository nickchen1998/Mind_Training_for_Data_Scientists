# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:35:45 2021

@author: nick
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
res = requests.get(url)
datas = BeautifulSoup(res.text, "lxml").find_all("div", class_="release_info")

movie_list = []

for item in datas:
    movie_list.append([])
    movie_list[len(movie_list)-1].append(item.find_all("a", class_="gabtn")[0].text.replace("\n", "").replace(" ", "")) # 加入中文名稱
    movie_list[len(movie_list)-1].append(item.find_all("a", class_="gabtn")[1].text.replace("\n", "").replace(" ", "")) # 加入英文名稱
    movie_list[len(movie_list)-1].append(item.find("div", class_="release_movie_time").text[7:]) # 加入上映日期
    
    if item.find("div", class_="leveltext") == None:
         movie_list[len(movie_list)-1].append(None)
    else:
        movie_list[len(movie_list)-1].append(item.find("div", class_="leveltext").find("span").text) # 加入期待度

columns = ["中文名稱", "英文名稱", "上映日期", "期待度"]
df = pd.DataFrame(movie_list, columns=columns)

print(df)
    