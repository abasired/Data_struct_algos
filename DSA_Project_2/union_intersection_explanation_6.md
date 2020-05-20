To compute the union of two linked list, we create a combined two list by appending one list to another and scan over the entire combined list to obtain a union of two lists. is_value_present method is used to avoid duplications in the union. 

On the other hand to compute intersection of two list, we use the union to get combined list of both list and loop over each element to check if it is both the lists. This has same time complexity as union of lists.   

### complexity analysis
1. Time complexity is $O(n)$ 
2. Space Complexity is $O(n)$