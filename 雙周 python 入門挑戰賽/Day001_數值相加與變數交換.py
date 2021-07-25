# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 08:30:58 2021

@author: nick
"""


print('------------作業 #01-1： 數值相加------------------')
a = eval(input('請輸入一個數字: '))
b = eval(input('請輸入一個數字: '))
sum = a + b

print(sum)

print('------------作業 #01-2： 數值相加------------------')
a = eval(input('請輸入一個數字: '))
b = eval(input('請輸入一個數字: '))

print('數字交換前: {}, {}'.format(a, b))
a, b = b, a

print("數字交換後: {}, {}".format(a, b))

print('------------作業 #01-2： 數值相加(正規寫法)---------')
a = eval(input('請輸入一個數字: '))
b = eval(input('請輸入一個數字: '))
print('數字交換前: {}, {}'.format(a, b))

tmp = a
a = b
b = tmp

print("數字交換後: {}, {}".format(a, b))