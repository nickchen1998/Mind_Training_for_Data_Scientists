# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 20:43:36 2021

@author: nick
"""


### 挑戰 #04-1：挑出重複出現的元素
### 挑戰 #04-2：重複元素計數
# 建立測試串列
test_list = [[1, 3, 1, 2, 2, 4, 5, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

## 方法一
# 由於有兩組測試 list 因此最外層使用迴圈
print('-----方法一-----')

for i in range(len(test_list)):
    x = sorted(test_list[i])
    
    # 創建一個保存數字出現次數的計次串列病例用迴圈統計出現次數
    count_list = [0]*len(x)
    for j in range(1, len(x)):
        if x[j] == x[j-1]:
            count_list[j] = 1 + count_list[j-1]
    
    repeat_list = []
    repeat_dic = {}
    
    for j in range(len(count_list)):
        if count_list[j] == 1:
            # 挑戰題 04-1 部分，印出重複字元
            repeat_list.append(x[j])
            
            # 挑戰題 04-2 部分，用字典印出重複字元出現次數
            repeat_dic[x[j]] = count_list[j] + 1
            
        # 如果大於 2 則代表不只出現一次，利用字典特性，可以直接覆蓋 value 的值
        elif count_list[j] >= 2:
            repeat_dic[x[j]] = count_list[j] + 1
    print(repeat_list)
    print(repeat_dic)
    print()
    
# 方法二
# 由於有兩組測試 list 因此最外層使用迴圈
print('-----方法二-----')

for i in range(len(test_list)):
    x = sorted(test_list[i])
    
    repeat_list = []
    repeat_dic = {}
    
    for j in range(len(x)):
        if x.count(x[j]) != 1:
            if x[j] not in repeat_list:
                # 挑戰題 04-1 部分，印出重複字元
                repeat_list.append(x[j])
                
                # 挑戰題 04-2 部分，用字典印出重複字元出現次數
                repeat_dic[x[j]] = x.count(x[j])
    
    print(repeat_list)
    print(repeat_dic)
    print()

# 方法三
print('-----方法三-----')

from collections import Counter

# 製圖用
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 由於有兩組測試 list 因此最外層使用迴圈
for i in range(len(test_list)):
    temp = Counter(sorted(test_list[i]))
    
    repeat_list = []
    repeat_dic = {}
    
    for key, value in temp.items():
        if value != 1:
            # 挑戰題 04-1 部分，印出重複字元
            repeat_list.append(key)
            
            # 挑戰題 04-2 部分，用字典印出重複字元出現次數
            repeat_dic[key] = value
    
    print(repeat_list)
    print(repeat_dic)
    print()
    
    # 練習使用 matplotlib 製圖
    plt.subplot(2, 1, i+1)
    labels = [key for key, value in temp.items()]
    sizes = [value for key, value in temp.items()]
    plt.title('第 {} 筆測試資料'.format(i+1))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')

plt.show()



