In implementing Huffman encoding and decoding we follow below steps:

1.Take a string and determine the relevant frequencies of the characters.
2.Build and sort a list of tuples from lowest to highest frequencies.
3.Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. 
4.Trim the Huffman Tree 
5.Encode the text into its compressed form.
6.Decode the text from its compressed form.

Details of each of the above steps are commented in code.

### complexity analysis
1. Time complexity is $O(n\log(n))$ as it involves sorting for encoding
2. Space Complexity is $O(n)$

$n$ is the number of unique charecters in sentence.