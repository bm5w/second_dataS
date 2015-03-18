[![Travis](https://travis-ci.org/bm5w/second_dataS.svg?branch=master)](https://travis-ci.org/bm5w/second_dataS.svg?branch=master)

Insertion Sort: This method will sort a list of numbers (int and floats). Insertion sort works with time complexity O(n) in the best case scenario. In the worse case, where the list is in reverse order and every value must be compared against every other number, the time complexity is O(n^2). It works well for lists that are already partially sorted. It can also sort the list as it receives it.
Merge Sort: This method will sort a list of numbers using merge sort. Merge sort works with a time complexity O(n) in the best case scenario. In the worse case, where the list is in reverse order, the time complexity is O(nLog(n)). Merge sort is a stable sort algorithm, meaning that it keeps the order of identical items in the list. This implementation is ~100 times faster than insertion sort, regardless of input.

### Data structures 

- [Binary Search Tree](https://github.com/bm5w/second_dataS/blob/master/bst.py)
  - An implementation of a BST utilizing a dictionary of dictionaries to keep track of each node and it's left and right children. While this is an unordinary method, where the ordinary method would use a linked list type structure, this method allows for O(1) for 'contains' methods, quick size methods. The downside of this approach is that recursive methods for finding depth and inserting nodes are not as readable and helper methods are required.
- [Hash Table](https://github.com/bm5w/second_dataS/blob/master/hash.py)
