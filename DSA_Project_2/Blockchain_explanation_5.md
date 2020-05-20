In the BlockChain program code, we implement a class with all basic functions needed for Blockchain. It is implemented as linked list with each block node. The crux of this implementation is the notion of prepending each new Block(node) to the head of the list and have the head refer to this new Block.

### complexity analysis
1. Time complexity is $O(n)$ as search goes over entire chain
2. Space Complexity is $O(n)$