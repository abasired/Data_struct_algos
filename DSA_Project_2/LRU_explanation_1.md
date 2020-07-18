In LRU cache implementation, we use below data structures
 *Dictionary: key value pair for cache access. 
 *Dictionary: To access respective node for each key. 
 *Doubly linked list: To adjust priority. 

In this program, we maintain a doubly linked list of all nodes in an order with last node corresponding to least priority(each corresponding to values in cache respectively). The major reason for choosing a doubly linked list is that, prepending a known node has O(1) time complexity. Further in-order to obtain node information in O(1), we used a dictionary to look it up based on key. 

### complexity analysis
1. Time complexity is $O(1)$
2. Space Complexity is $O(n)$