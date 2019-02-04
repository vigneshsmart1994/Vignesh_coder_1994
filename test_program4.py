# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:44:04 2019

@author: Vicky
"""

mylist=list(input("data... ").split(","))
b1=0
b2=0
bt1=""
bt2=""
i=1
cc=0
for r in mylist:
    if i==1:
       b1=b1+int(r)
       bt1=bt1 + (r) + " + "
       if(int(r)==1 or int(r)==3):
           i=2
    else:
        b2=b2+int(r)
        bt2=bt2 + (r) + " + "
        if(int(r)==1 or int(r)==3):
           i=1
    cc=cc+1
    if(cc==6):
        cc=0
        if(i==1):
            i=2
        else:
            i=1            
print(str(b1) + "(" + bt1 + ")")
print(str(b2) + "(" + bt2 + ")")       
       
       
