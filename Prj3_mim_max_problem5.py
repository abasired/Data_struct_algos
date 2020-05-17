#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:42:11 2020

@author: ashishbasireddy
"""

def get_min_max(ints):
    
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_index = 0 
    max_index = 0
    index = 1
    
    while index < len(ints):
        if ints[min_index] > ints[index]:
            min_index = index
        
        if ints[max_index] < ints[index]:
            max_index = index
        
        index += 1
    
    return(ints[min_index],ints[max_index])

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 50)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 49) == get_min_max(l)) else "Fail")