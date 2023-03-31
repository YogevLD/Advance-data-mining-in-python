#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:16:00 2023

@author: yogevladani
"""


###################### part 1  ######################
def revword(word:str):
    word=word.lower()[::-1]
    return word
print(revword("Hello"))
###################### part 2  ######################
def countword():
    file= open("text.txt")
    line_list=[]
    for line in file:
        line_list.append(line.rstrip().split()) 
    dic={line_list[0][0]:1} 
    for sentence in line_list[1:]:
        for word in sentence:
            dic[revword(word)]=dic.get(revword(word),0)+1
    
    return dic[line_list[0][0]]

print(countword())

            