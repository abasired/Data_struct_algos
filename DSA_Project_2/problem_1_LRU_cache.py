class Node:  #node of a linked list
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        

class LinkedList: #linked list with prepend, prioritize and remove_last_node methods
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self, value):
        
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node       
    
    def prioritize(self, node):
        """
        In this method,we prepend input node to the start of linked list and adjust the link between
        adjacent nodes of input node. This method has time complexity of O(1)
        """
        
        if node is self.tail:
            self.prepend(node.value)
            self.remove_last_node()
        elif node is not self.head:
            node.previous.next = node.next
            node.next.previous = node.previous
            self.prepend(node.value)
        
    
    def remove_last_node(self):
        
        self.tail = self.tail.previous
         

        

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        """
        dict is Dictionary used for retrieving key value pair.
        prioritynode_list is a Dictionary comprising of keys and respective nodes.
        Each node has value and both adjacent nodes information as attributes.
        Linked_list is Doubly linked list comprising of least priority node as last node.
        """
        self.capacity = capacity
        self.num_elements = 0
        self.dict = {}          #key value pair for lookup O(1)
        self.prioritynodelist = {}  # To adjust priority and retrive node in O(1)
        self.linked_list = LinkedList()

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent.      
        Time complexity is O(1), as put() has time complexity of O(1)
        """
        
        if key in self.dict.keys():
            self.put(key, self.dict[key])
            return self.dict[key]
        else:
            self.put(key, key)
            return -1

    def put(self, key, value):
        
        # 
        if key in self.prioritynodelist.keys():
            self.linked_list.prioritize(self.prioritynodelist[key])
        else:
            if self.num_elements >= self.capacity:
                self.prioritynodelist.pop(self.linked_list.tail.value)
                self.dict.pop(self.linked_list.tail.value)
                self.linked_list.remove_last_node()
            else:
                self.num_elements += 1

            self.linked_list.prepend(value)
            self.dict[key] = value
            self.prioritynodelist[key] = self.linked_list.head        


our_cache = LRU_Cache(5)

print(our_cache.get(3))         #empty cache
our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);
print(our_cache.get(4)) 

#print(our_cache.get(1))       # returns 1
#print(our_cache.get(2))       # returns 2
#print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.put(5, 5) 
our_cache.put(6, 6)

#print(our_cache.get(4))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
#print(our_cache.dict)