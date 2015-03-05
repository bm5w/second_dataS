class bst():
    def __init__(self):
        '''Initialize a bst with a start value and dictionary of nodes.'''
        self.start = None
        self.nodes = {}

    def _insert(self, node, val):
        '''Recursive helper method for insert.'''
        if node < val:
            if self.nodes[node]['right'] is None:
                self.nodes[node]['right'] = val
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
        '''Reursive helper method for depth.'''
        _node = self.nodes.get(node)
        if _node is None:
            return 0
        if (_node['left'] is None) and (_node['right'] is None):
            return 1
        left = self._depth(self.nodes[node]['left'])
        right = self._depth(self.nodes[node]['right'])
        return 1 + max(left, right)

    def depth(self):
        '''Returns the total number of levels in the tree.'''
        return self._depth(self.start)

    def balance(self):
        '''Returns a positive or negative value representing the bst balanced.'''
        if self.start is None:
            return 0
        depth_left = self._depth(self.nodes[self.start]['left'])
        depth_right = self._depth(self.nodes[self.start]['right'])
        return depth_left-depth_right
