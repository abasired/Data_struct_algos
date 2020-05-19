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
    start_number = 0 
    end_number = number
    middle_number = (start_number + end_number)//2
    
    if number == 0 or number == 1:
        return number
    
    while middle_number > 0:
        #print(sq_root)
        #print(middle_number)
        if (middle_number * middle_number == number) or (middle_number * middle_number < number and (middle_number+1) * (middle_number+1) > number) :
            
            return middle_number
        
        
        if middle_number * middle_number > number:
            end_number = middle_number-1
        else:
            start_number = middle_number+1
        
        middle_number = (start_number + end_number)//2
           

#print ("Pass" if  (3 == sqrt(9)) else "Fail")
#print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (4 == sqrt(25)) else "Fail")
#print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")