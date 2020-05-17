#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:59:49 2020

@author: ashishbasireddy
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    sq_root = number
    search_list = []
    
    while True:
        #print(sq_root)
        if (sq_root * sq_root == number) or (sq_root * sq_root < number and (sq_root+1) * (sq_root+1) > number) :
            return sq_root
        
        
        if sq_root * sq_root > number:
            sq_root = sq_root//2
            search_list.append(sq_root)
        else:
            sq_root += max(1,sq_root//4)
            if sq_root in search_list:
                sq_root -= 1
                search_list.append(sq_root)
            else:
                search_list.append(sq_root)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(25)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")