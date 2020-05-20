#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:25:34 2020

@author: ashishbasireddy
"""
    
import sys

class Node:
    
    def __init__(self, value, char):
        self.value = value
        self.char = char
        self.next = None
        self.left = None
        self.right = None
        
    def set_left_child(self,node):
        self.left = node
    
    def set_right_child(self,node):
        self.right = node
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def is_leaf_node(self):
        return bool(self.char)


        
class Linked_list:
    
    def __init__(self):
        self.head = None
        self.tail = None
     
    def append(self, node):

        if self.head is None:
            self.head = node
            self.tail = self.head
            return

        self.tail.next = node
        self.tail = node
        
    def insert_node(self, node):
        
        current_node = self.head
        previous_node = current_node
        
        if self.head == None:
            self.head = node
        elif node.value < self.head.value:
                node.next = self.head
                self.head = node
        elif node.value >= self.tail.value:
            self.append(node)
            
        else:
            while node.value >= current_node.value:
                    previous_node = current_node
                    current_node = current_node.next
                    #print(current_node.char,current_node.value)
            
            previous_node.next = node
            node.next = current_node
    
    
class Tree:
    
    def __init__(self, node):
        self.root = node
        
    def get_root(self):
        return self.root


def path_from_node_to_root(root, data):

    if root.is_leaf_node():        
        if root.char == data:
            return ''
        else:
            return None
    
    #print(root.get_left_child().value)

    left_answer = path_from_node_to_root(root.get_left_child(), data)
    if left_answer is not None:
        return left_answer + '0'

    right_answer = path_from_node_to_root(root.get_right_child(), data)
    if right_answer is not None:
        return right_answer + '1'
    
    return None

def huffman_encoding(data):
    
    if len(data) == 0:
        return '',Tree(Node(-1," "))
    
    if len(data) == 1:
        return str(1), Tree(Node(1,data))
        
    freq_dict = dict()
    code_dict = dict()

    for char in data:
        if char in freq_dict.keys():
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
           
    freq_sorted = sorted(zip(freq_dict.values(), freq_dict.keys()))
    sorted_linked_list = Linked_list()

    for i in range(len(freq_sorted)):
        node = Node(freq_sorted[i][0], freq_sorted[i][1])
        sorted_linked_list.append(node)

    while sorted_linked_list.head.next:
        new_node = Node(sorted_linked_list.head.value + sorted_linked_list.head.next.value, None)
        new_node.set_left_child(sorted_linked_list.head)
        new_node.set_right_child(sorted_linked_list.head.next)

        sorted_linked_list.insert_node(new_node)
        sorted_linked_list.head = sorted_linked_list.head.next.next
    
    Huffman_tree = Tree(sorted_linked_list.head)
    encoded_data = ''
    
    for char in data:
        code_dict[char] = path_from_node_to_root(Huffman_tree.get_root(), char)
        encoded_data += str(code_dict[char][::-1])
    
    return encoded_data, Huffman_tree

def huffman_decoding(encoded_data,Huffman_tree):
    decoded_data = ''
    node = Huffman_tree.get_root()
    
    if len(encoded_data) == 0:
        return 'sentence is empty'
    
    if len(encoded_data) == 1:
        return node.char
    
    for char in encoded_data:
    
        if char is '0':
            node = node.get_left_child()
        else:
            node = node.get_right_child() 
        #print(char)
        if node.is_leaf_node():
            #print(node.char)
            decoded_data += node.char
            node = Huffman_tree.get_root()
    
    return decoded_data

if __name__ == "__main__":
    codes = {}

    #a_great_sentence = "The bird is the word"
    #a_great_sentence = ""
    #a_great_sentence = "h"
    #a_great_sentence = "hello"

    #print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    