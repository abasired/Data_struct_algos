#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:14:57 2020

@author: ashishbasireddy
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1
    
    while start_index <= end_index :
        
        middle_index = (start_index + end_index)//2
        #print(middle_index)
        #print(input_list[middle_index])
        
        if input_list[middle_index] == number:
            return middle_index
        
        # Check to see if the sub-array is sorted array
        if input_list[middle_index] > input_list[start_index]:
            
            # Check whether number is in the sorted array
            if number < input_list[middle_index] and number >= input_list[start_index] :
                end_index = middle_index - 1
            else:
                 start_index = middle_index + 1
        else: # smaller rotated array
            if number > input_list[middle_index] and number <= input_list[end_index]:
                start_index = middle_index + 1
            else:
                end_index = middle_index - 1
        
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

#test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
#test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[9,3], 2])
test_function([[], 1])