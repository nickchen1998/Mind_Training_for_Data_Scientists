# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:44:27 2021

@author: nick
"""

from selenium import webdriver
from time import sleep
import pandas as pd




driver = webdriver.Chrome('C:/Users/nick/Desktop/chromedriver.exe')
driver.get("https://hiskio.com/")
sleep(5)


class_list = []
new_class = driver.find_elements_by_class_name("grid-cols-1")[1].find_elements_by_xpath(".//li/a/div[1]/div[2]/h3")
teacher_name = driver.find_elements_by_class_name("grid-cols-1")[1].find_elements_by_xpath(".//li/a/div[1]/div[2]/div[2]/p[1]")
class_price = driver.find_elements_by_class_name("grid-cols-1")[1].find_elements_by_xpath(".//li/a/div[1]/div[2]/div[2]/p[2]")

for i in range(len(new_class)):
    class_list.append([])
    class_list[len(class_list)-1].append(new_class[i].text)
    class_list[len(class_list)-1].append(teacher_name[i].text)
    class_list[len(class_list)-1].append(class_price[i].get_attribute('textContent').replace("\n", ""))

driver.close()

columns = ["課程名稱", "老師名稱", "課程價格"]
df = pd.DataFrame(class_list, columns=columns)
print(df)

# 碰到問題: 有找到元素但是吐回空值
# 解決辦法: .get_attribute('textContent')
# 參考資料: https://blog.csdn.net/JustZzer/article/details/111355510