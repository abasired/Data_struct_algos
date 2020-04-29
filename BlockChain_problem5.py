#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:07:38 2020

@author: ashishbasireddy
"""

import hashlib
import datetime 

def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:
    
    def __init__(self, data, previous_hash):
        
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = calc_hash(str(data))
    

class BlockChain:

    def __init__(self):
        self.head = None

    def append(self, data,previous_hash):
        
        if self.head is None:
            self.head = Block(data,0)
            return

        new_head = Block(data,self.head.hash)
        new_head.previous_block = self.head
        self.head = new_head
       
    def size(self):
        
        size = 0
        block = self.head

        while block:
            size += 1
            block = block.previous_block
            return size
    
    def search(self, data):
        
        if self.head is None:
            return False
        
        head = self.head
        
        while head.previous_hash != 0:
            
            if head.data == data:
                return True
            head = head.previous_block
            
        return False

    def to_list(self):
        out = []
        block = self.head

        while block:
            out.append(block)
            block = block.previous_block

        return out
  