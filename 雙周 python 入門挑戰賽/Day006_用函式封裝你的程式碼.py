# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:40:31 2021

@author: nick
"""


# 挑戰 #06-1：用函式封裝你的程式碼 - 基礎
class cSum:
    # 方法一 for 迴圈
    def use_for(x):
        tmp = 0
        for i in x:
           tmp += 1
        
        return tmp
    # 方法二 sum 方法
    def use_sum(x):
        return sum(x)
    
    # 方法三 動態參數
    # 補充: * 為打包成 tuple ** 為打包成字典
    def use_arg(*arg):
        return sum(arg)
    
# 建立測試資料
test_data_1 = [1, 2, 3]
test_data_2 = [1, 2, 3, 4 ,5]

print(cSum.use_for(test_data_1))
print(cSum.use_sum(test_data_2))
print(cSum.use_arg(1, 2, 3, 4, 5, 6, 7, 8, 9))

# 挑戰 #06-2：用函式封裝你的程式碼 - 進階
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
    return result
    
def find_max_distence(x):
    # 存放兩兩自餘數相減後的結果
    tmp = []
    for i in range(1, len(x)):
        tmp.append(x[i]-x[i-1])
        
    # 根據邏輯推斷，tmp 第一個位置為 index[i+1] - index[i]
    # 因此要找相減區間最大，只須找到最大值的位置，並且對應到 result 的相關位置即可
    return x[tmp.index(max(tmp))], x[tmp.index(max(tmp))+1]


result = self_dividing_number(11, 20)
print(find_max_distence(result))
result = self_dividing_number(100, 900)
print(find_max_distence(result))

