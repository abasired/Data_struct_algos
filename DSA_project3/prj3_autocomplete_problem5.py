#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:49:16 2020

@author: ashishbasireddy
"""

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.is_word = True 

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        
        if prefix is '':
            return None
        else:
            for char in prefix:
                if char in node.child.keys():
                    node = node.child[char]
                else:
                    return None
        #print(list(node.child.keys()))
        #print(node.is_word)
        return node

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.child = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.child[char] = TrieNode()
        
    def suffixes(self):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffix_list = []
        temp_list = list()
        
        if not self.child and self.is_word:
            return []
        
        if self.is_word:
            suffix_list.append("")
        
        for element in self.child:
            #print(element)
            node = self.child[element]
            temp_list = node.suffixes()
            
            if len(temp_list) > 0:
                for each_list in temp_list:
                    #print(each_list)
                    suffix_list.append(element + each_list )
            else:
                suffix_list.append(element)
            
        return suffix_list
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
f("fu")
f("")
f("ku")