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
    path_list = []
        
    for name in file_name:
        
        if os.path.isdir(os.path.join(path, name)):
            temp_list = find_files(suffix ,os.path.join(path, name))
            path_list = path_list + temp_list
        elif os.path.isfile(os.path.join(path, name)):
            if suffix in name:
                path_list.append(os.path.join(path, name))
            
        
    return path_list

#use appropiate path while verifying this code. This path is local path
path = os.environ['HOME'] + "/testdir"


#recursion based search
#print(find_files(".c", path))     # search for .c files
#print(find_files(".py", path))    # search for .py files
print(find_files(".h", path))     # search for .h files

#loops to implement a simialr search.
os.chdir(path)

for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
       if '.h' in name:
           print(os.path.join(root, name))
      

    