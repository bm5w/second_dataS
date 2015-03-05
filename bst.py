class bst():
    def __init__(self):
        self.start = None
        self.nodes = {}
        self.depth = None

    def _insert(self, node, val, depth):
        """Recursive helper method for insert."""
        if node < val:
            if self.nodes[node]['right'] is None:
                self.nodes[node]['right'] = val
                self.nodes[val] = {'left': None, 'right': None}
            else:
                self._insert(self.nodes[node]['right'], val)
        else:
            if self.nodes[node]['left'] is None:
                self.nodes[node]['left'] = val
                self.nodes[val] = {'left': None, 'right': None}
            else:
                self._insert(self.nodes[node]['left'], val)

    def insert(self, val):
        '''Insert a value into the bst unless already present.'''
        if self.nodes.contains(val):
            return None
        if self.start is None:
            self.start = val
            self.nodes[val] = {'left': None, 'right': None}
        else:
            self.depth = self._insert(self.start, val)

    def contains(self, val):
        '''Will return True if the value is in the bst.'''
        return val in self.nodes

    def size(self):
        '''Will return the size of the bst, equal to the total # vals.'''
        return len(self.nodes)

    def _depth(self, node):
        '''Helper method for depth.'''
        if node is None:
            return 0
        if self.nodes[node]['left'] and self.nodes[node]['right'] is None:
            return 1
        return 1 + max(self._depth(self.nodes[node]['left']), self._depth(self.nodes[node]['right']))

    def depth(self):
        '''Returns the total number of levels in the tree.'''
        return self._depth(self.nodes[self.start])

    def balance(self):
        '''Returns a positive or negative value representing the bst balanced.'''
        depth_left = self._depth(self.nodes[self.start]['left'])
        depth_right = self._depth(self.nodes[self.start]['right'])
        return depth_left-depth_right
