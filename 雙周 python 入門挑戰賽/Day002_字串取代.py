# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:22:54 2021

@author: nick
"""

#挑戰 #02-1： 字串取代（基礎版）
s = 'This company is not good at all.'

#方法一
print(s.replace('not good at all', 'good'))

#方法二
s = s.split(' ')
s.remove('not')
s.remove('at')
s.remove('all.')

#組合字串並印出
for i in range(len(s)):
    #判斷是否為結尾
    if i == len(s)-1:
        print(s[i] + '.')
    else:
        print(s[i], end=' ')

#挑戰 #02-2： 字串取代（進階版）
#建立題目指定測試字串
test_string = ['This company is not good at all', 'I’m not at all happy about it']
 
#方法一
import re

#建立正規表達式的規則
pattern = r"not.+all"

#利用 re.sub 方法進行字串的替換
for i in range(len(test_string)):
    result = re.sub(pattern, 'good', test_string[i])
    print(result + '.')

#方法二
#由於題目的範例輸入不只一個，因此最外層使用迴圈進行撰寫
#此方法不能用於判斷文章，只能單獨判斷一行字串
for i in range(len(test_string)):
    string =test_string[i].split(' ')
    
    index = string.index('not')
    
    #當 all 還在字串內，表示刪除需要持續進行
    while ('all' in string):
        del string[index]
        #如果 all 不在字串裡面，即跳出迴圈
        if 'all' not in string:
            break
    
    #將原本 not 的位置插入字串 good，若發生錯誤，代表原本位置為空值，直接將 good 插入尾端
    try:
        string.insert(index, 'good')
    except:
        string.append('good')
    
    #組合字串並印出
    for j in range(len(string)):
        #判斷是否為結尾，是的話加上句號
        if j == len(string)-1:
            print(string[j] + '.')
        else:
            print(string[j], end=' ')


