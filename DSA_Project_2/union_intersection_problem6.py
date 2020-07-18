#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:17:00 2020

@author: ashishbasireddy
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        node = Node(value)
        self.tail.next = node
        self.tail = node
        

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def is_value_present(self,value):
        
        node = self.head
        
        while node:
           #scan through the linked list 
            #print(node.value)
            if node.value == value:
                return True
            else:
                node = node.next
        
        return False
      
            

def union(llist_1, llist_2):
    # Your Solution Here
    
    temp_list = LinkedList()
    union_list = LinkedList()
    
    assert llist_1.size() > 0 and llist_2.size() > 0, "lists are empty"
    
    
    node1 = llist_1.head
    node2 = llist_2.head
    
    for i in range(llist_1.size()):
        temp_list.append(node1.value)
        node1 = node1.next
     
    for i in range(llist_2.size()):
        temp_list.append(node2.value)
        node2 = node2.next

    node = temp_list.head
    for i in range(temp_list.size()):
        if i == 0:
            union_list.append(node.value)
        else:
            if not union_list.is_value_present(node.value):
                union_list.append(node.value)
        node = node.next
        
    return union_list   


def intersection(llist_1, llist_2):
    # Your Solution Here
    
    union_list = union(llist_1, llist_2)

    intsec_list = LinkedList()
    
    node = union_list.head
    
    for i in range(union_list.size()):
        if (llist_1.is_value_present(node.value) and llist_2.is_value_present(node.value)) :
            intsec_list.append(node.value)   
        node = node.next
        
            
    return intsec_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

element_1 = []
element_2 = [1,5,7,9]

element_1 = [1,4,8,2]
element_2 = []

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

#print (union(linked_list_1,linked_list_2))
#print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

#element_1 = [3,2,4,35,6,65,6,4,3,23]
#element_2 = [1,7,8,9,11,21,1]



for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

#print (union(linked_list_3,linked_list_4))
#print (intersection(linked_list_3,linked_list_4))