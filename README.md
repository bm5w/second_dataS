# second_dataS
[![Travis](https://travis-ci.org/bm5w/second_dataS.svg?branch=master)](https://travis-ci.org/bm5w/second_dataS.svg?branch=master)
BST (Binary Search Tree): An implementation of a BST utilizing a dictionary
of dictionaries to keep track of each node and it's left and right children.
While this is an unordinary method, where the ordinary method would use a
linked list type structure, this method allows for O(1) for 'contains' methods,
quick size methods. The downside of this approach is that recursive methods
for finding depth and inserting nodes are not as readable and helper methods
are required.