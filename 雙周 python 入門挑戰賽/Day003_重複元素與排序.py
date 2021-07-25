# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 08:56:11 2021

@author: nick
"""
# 挑戰 #03-1：重複元素與排序
# 建立測試串列
test_list = [[1, 3, 1, 2, 2, 4, 5, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# 方法一
# 由於有兩組測試 list 因此最外層使用迴圈
for i in range(len(test_list)):
    x = sorted(test_list[i], reverse=True)
    count_list = [0]*len(x)

    for j in range(1, len(x)):
        if x[j] == x[j-1]:
            count_list[j] = 1 + count_list[j-1] # 順便計算眾數
    
    tmp = 0
    while True:
        if tmp == len(x):break
        if count_list[tmp] > 0:
            x.pop(tmp)
            count_list.pop(tmp)
        else:
            tmp += 1
    
    print(x)

# 方法二
# 由於有兩組測試 list 因此最外層使用迴圈
for i in range(len(test_list)):
    x = sorted(test_list[i], reverse=True)
    tmp = 0
    
    while True:
        if tmp == len(x):break
        if x.count(x[tmp]) != 1:
            x.pop(tmp)
            continue
        else:
            tmp += 1
    
    print(x)

# 方法三
# 由於有兩組測試 list 因此最外層使用迴圈
for i in range(len(test_list)):
    # 集合內不會有重複元素，但返回的為集合物件，因此再重新導回 list
    x = list(set(test_list[i]))
    print(sorted(x, reverse=True))
    
# 挑戰 #03-2：字典合併
# 建立測試字典
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}   
 
# 方法一
d = {**dic1, **dic2, **dic3}
print(d)

# 方法二
d = dic1.copy()
d.update(dic2)
d.update(dic3)
print(d)

# 方法三
# 其實和方法二一樣只是會更改原有 dic1 內容所以放最後寫
# 補充: dic1.update(dic2)返回的為 NoneType
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    