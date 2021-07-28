# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:01:07 2021

@author: nick
"""

from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd


def find_movie(url):
    driver = webdriver.Chrome('C:/Users/nick/Desktop/chromedriver.exe')
    driver.get(url)
    movie_list = []
    
    while True:
        page_content = driver.page_source
        index_result = soup(page_content, 'lxml')
        datas = index_result.find_all("div", class_="release_info")
        
        for item in datas:
            movie_list.append([])
            movie_list[len(movie_list)-1].append(item.find_all("a", class_="gabtn")[0].text.replace("\n", "").replace(" ", "")) # 加入中文名稱
            movie_list[len(movie_list)-1].append(item.find_all("a", class_="gabtn")[1].text.replace("\n", "").replace(" ", "")) # 加入英文名稱
            movie_list[len(movie_list)-1].append(item.find("div", class_="release_movie_time").text[7:]) # 加入上映日期
        
        if item.find("div", class_="leveltext") == None:
             movie_list[len(movie_list)-1].append(None)
        else:
            movie_list[len(movie_list)-1].append(item.find("div", class_="leveltext").find("span").text) # 加入期待度
        
        try:
            next_page_btn = driver.find_element_by_xpath("//li[@class='nexttxt']/a")
            next_page_btn.click()
        except:
            break
        
    driver.close()
    return movie_list

result = find_movie("https://movies.yahoo.com.tw/movie_comingsoon.html")

columns = ["中文名稱", "英文名稱", "上映日期", "期待度"]
df = pd.DataFrame(result, columns=columns)

print(df)



