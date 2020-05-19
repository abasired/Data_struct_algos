#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:58:56 2020

@author: ashishbasireddy
"""

## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.children['/'] = RouteTrieNode()
        self.root.handler = handler
        
    def insert(self, path):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        path_list = list()
        path_list = path.split('/')
        while '' in path_list:
            path_list.remove('')
        node = self.root.children['/']
        
        for word in path_list:
            if word not in node.children:
                node.children[word] = RouteTrieNode()
            node = node.chidren[word]
        
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        path_list = path.split('/')
        while '' in path_list:
            path_list.remove('')
        path_list = ['/'] + path_list
        node = self.root
                               
        for word in path_list:
            if word not in node.children:
                return None
            node = node.children
        return node.handler   

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, string):
        # Insert the node as before
        self.children[string] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.RouteTrie = RouteTrie(handler)
        
    def add_handler(self,path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        node = self.RouteTrie.root
        index = 0
        
        for word in path_list:
            
            if word not in node.children:
                node.children[word] = RouteTrieNode()
            
            if index == len(path_list) - 1:
                node.handler = handler
            else:
                index += 1
            
            node = node.children[word]

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        node = self.RouteTrie.root
        index = 0
        
        for word in path_list:
            if word not in node.children:
                return None
            
            if index == len(path_list) - 1:
                return node.handler
            else:
                index += 1
            node = node.children[word]
            
        return node.handler   

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = list()
        path_list = path.split('/')
        while '' in path_list:
            path_list.remove('')
        path_list = ['/'] + path_list
        #print(path_list)
        return path_list 

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

                     