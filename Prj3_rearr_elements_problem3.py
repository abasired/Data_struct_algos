#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:44:18 2020

@author: ashishbasireddy
"""

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = list()
    sorted_list = mergesort(input_list)
    #print(sorted_list)
    int1 = 0
    int2 = 0
    largest_index = 0
    
    while len(input_list) < 2:
        input_list.append(0)
    
    
    if len(sorted_list) % 2 != 0:
        largest_index = sorted_list.pop(-1)

    #print(sorted_list)
    for i in range(len(sorted_list)//2):
        int1 += sorted_list[2*i]* (10**i)
        int2 += sorted_list[2*i+1]* (10**i)
    
    if largest_index:
        int2 += largest_index * (10**(len(sorted_list)//2))
    
    #print(int1)
    #print(int2)
    return [int2, int1]
    
input_list = [1, 2, 3, 4, 5]
rearrange_digits(input_list)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
#test_case = [[4], [4, 0]]
#test_case = [[], [0, 0]]
test_function(test_case)

