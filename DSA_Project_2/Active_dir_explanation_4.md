The active directory problem is a straight fwd application of recursion. 
Basically, in a group comprising of subgroups and users, the idea is to check if the user is among the list of users(base case) or repeat the process in each of the subgroup(recursive call). The code is self explanatory using recursion. 

### complexity analysis
1. Time complexity is $O(n)$ 
2. Space Complexity is $O(n)$