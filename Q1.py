#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:00:48 2023

@author: yogevladani
"""

"""opthion 1"""
def my_func (x1,x2,x3):
    try:
        denomiator=x1+x2+x3
        numerator=(x1+x2+x3)*(x2+x3)*x3
        if isinstance(x1,int) or isinstance( x2,int) or isinstance (x3,int):
           return ("Error: parameters should be float")
        elif denomiator==0:
           return ("Not a number – denominator equals zero")
            
        else:
           numerator= denomiator*(x2+x3)*x3
           return float(numerator/denomiator)
    except:
        return None 
    
            
my_func("sss", 6.0, 3.0) 

"""opthion 2"""
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
    
my_func1(4.0,3.0, 3) """ 
