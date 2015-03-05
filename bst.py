# class node():

#     def __init__(self):
#         self.left = None
#         self.right = None
#         self.depth = 

class bst(): 

    def __init__(self):
        self.start = None

    def _insert(self, node, val):
        if node < val:
            if node.right is None:
                node.right = val
            else:
                self._insert(node.right, val)
        else:
            if node.left is None:
                node.left = val
            else:
                self._insert(node.left, val)

            


    def insert(self, val):
        '''Insert a value into the bst unless already present.'''
        if contains(val):
            return None
        if self.start = None:
            self.start = val
        else:
            self.insert(self.start, val)


    def contains(self, val):
        '''Will return True if the value is in the bst.'''
        pass

    def size(self):
        '''Will return the size of the bst, equal to the total # vals.'''
        pass

    def depth(self):
        '''Returns the total number of levels in the tree.'''
        pass

    def balance(self):
        '''Returns a positive or negative value representing the bst balanced.'''
        pass
