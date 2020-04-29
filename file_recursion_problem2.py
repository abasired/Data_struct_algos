#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:21:50 2020

@author: ashishbasireddy
"""
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    file_name = os.listdir(path)
        
    for name in file_name:
        
        if os.path.isfile(os.path.join(path, name)):
            if '.c' in name:
                print(os.path.join(path, name))
        elif os.path.isdir(os.path.join(path, name)):
            find_files(".c",os.path.join(path, name))
        
    return None

path = "/Users/ashishbasireddy/testdir"

#recursion based search
find_files("suffix", path)


#loops to implement a simialr search.
os.chdir(path)

for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
       if '.c' in name:
           #print(os.path.join(root, name))
      

    