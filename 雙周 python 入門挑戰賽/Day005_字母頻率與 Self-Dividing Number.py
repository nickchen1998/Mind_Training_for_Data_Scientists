# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 08:34:58 2021

@author: nick
"""
# 挑戰 #05-1：字母頻率與 Self-Dividing Number
test_str = 'Hello World'
# 方法一
from collections import Counter

# 只是單純想把輸出都弄成一樣才加這行，不然他會是一個 counter 物件
result = dict(Counter(test_str))

print(result)

# 方法二
result = {}

for i in test_str:
    try:
        result[i] += 1
    except:
        result[i] = 1

print(result)

# 方法三
result = {}
for i in test_str:
    # 補充: result.get() 不會更動原字典值 只會回傳 value
    result[i] = result.get(i, 0) + 1

print(result)

# 挑戰 #05-2：Self-Dividing Number
def self_dividing_number(x, y):
    # 存放自餘數用
    result = []
    
    # 處理區間
    for i in range(x, y+1):
        
        # 處理自餘數
        tmp = 1
        for j in str(i):
            try:
                if i % int(j) == 0: 
                    if tmp == len(str(i)):
                        result.append(i)
                    else: 
                        tmp += 1
                        continue      
                else:
                    break
            except:
                break
    
    # 存放兩兩自餘數相減後的結果
    tmp = []
    for i in range(1, len(result)):
        tmp.append(result[i]-result[i-1])
        
    # 根據邏輯推斷，tmp 第一個位置為 index[i+1] - index[i]
    # 因此要找相減區間最大，只須找到最大值的位置，並且對應到 result 的相關位置即可
    print(result[tmp.index(max(tmp))], result[tmp.index(max(tmp))+1])
    
self_dividing_number(11, 20)
self_dividing_number(100, 900)