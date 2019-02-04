# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:57:48 2019

@author: Vicky
"""
num=int(input("enter the no"))
for i in range(num):
    if(i%3==0 and i%5==0):
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
