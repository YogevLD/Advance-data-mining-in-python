#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:00:48 2023

@author: yogevladani
"""



def my_func1 (x1,x2,x3):
    if isinstance(x1,int) or isinstance( x2,int) or isinstance (x3,int):
       print("Error: parameters should be float")
    elif type(x1) !=float or type(x2) != float or type(x3) != float:
        print('None')
    elif (x1+x2+x3)==0:
        print("Not a number – denominator equals zero")
            
    else:
        denomiator=x1+x2+x3
        numerator=(x1+x2+x3)*(x2+x3)*x3
        numerator= denomiator*(x2+x3)*x3
        print(float(numerator/denomiator))
    
my_func1(4.0,3.0, -7)

