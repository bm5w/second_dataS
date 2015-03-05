class bst():
    def __init__(self):
        self.start = None
        self.nodes = {}

    def _insert(self, node, val):
        """Recursive helper method for insert."""
        if node < val:
            if self.nodes[node]['right'] is None:
                self.nodes[node]['right'] = val
                print 'val: {}'.format(val)
                print self.nodes[node]['right']
                self.nodes[val] = {'left': None, 'right': None}
            else:
                self._insert(self.nodes[node]['right'], val)
        else:
            # import pdb; pdb.set_trace()
            if self.nodes[node]['left'] is None:
                self.nodes[node]['left'] = val
                self.nodes[val] = {'left': None, 'right': None}
            else:
                self._insert(self.nodes[node]['left'], val)

    def insert(self, val):
        '''Insert a value into the bst unless already present.'''
        if self.contains(val):
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
        # if node is None:
        #     return
        print 'NODE: {}'.format(node)
        # import pdb; pdb.set_trace()
        if (self.nodes[node]['left'] is None) and (self.nodes[node]['right'] is None):
            return 1

        if self.nodes[node]['left'] is None:
            left = 0
        else:
            left = self._depth(self.nodes[node]['left'])

        if self.nodes[node]['right'] is None:
            right = 0
        else:
            right = self._depth(self.nodes[node]['right'])

        max_value = max(left, right)
        return 1 + max_value

    def depth(self):
        '''Returns the total number of levels in the tree.'''
        if self.start is None:
            return 0
        return self._depth(self.start)

    def balance(self):
        '''Returns a positive or negative value representing the bst balanced.'''
        if self.start is None:
            return 0
        depth_left = self._depth(self.nodes[self.start]['left'])
        depth_right = self._depth(self.nodes[self.start]['right'])
        return depth_left-depth_right
