import random


class bst():
    def __init__(self):
        '''Initialize a bst with a start value and dictionary of nodes.'''
        self.start = None
        self.nodes = {}

    def _insert(self, node, val):
        '''Recursive helper method for insert.'''
        if node < val:
            if self.nodes[node].get('right') is None:
                self.nodes[node]['right'] = val
                self.nodes[val] = {}
            else:
                self._insert(self.nodes[node]['right'], val)
        else:
            if self.nodes[node].get('left') is None:
                self.nodes[node]['left'] = val
                self.nodes[val] = {}
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
            self._insert(self.start, val)

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
        if (_node.get('left') is None) and (_node.get('right') is None):
            return 1
        left = self._depth(self.nodes[node].get('left'))
        right = self._depth(self.nodes[node].get('right'))
        return 1 + max(left, right)

    def depth(self):
        '''Returns the total number of levels in the tree.'''
        return self._depth(self.start)

    def balance(self):
        '''Returns a positive or negative val representing the bst balanced.'''
        if self.start is None:
            return 0
        depth_left = self._depth(self.nodes[self.start].get('left'))
        depth_right = self._depth(self.nodes[self.start].get('right'))
        return depth_left-depth_right

    def get_dot(self):
        '''Return the tree with root 'self' as a dot graph for visualization'''
        return "digraph G{\n%s}" % ("" if self.start is None else (
            "\t%s;\n%s\n" % (
                self.start,
                "\n".join(self._get_dot(self.start))
            )
        ))

    def _get_dot(self, node):
        """recursively prepare a dot graph entry for this node."""
        left = self.nodes[node].get('left')
        right = self.nodes[node].get('right')
        if left is not None:
            yield "\t%s -> %s;" % (node, left)
            for i in self._get_dot(left):
                yield i
        elif right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (node, r)
        if right is not None:
            yield "\t%s -> %s;" % (node, right)
            for i in self._get_dot(right):
                yield i
        elif left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (node, r)

    def print_dot(self):
        # To run me do this from cmd line: python bst.py > temp.png
        import subprocess
        dot_graph = self.get_dot()
        t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
        t.communicate(dot_graph)

    def _in_order(self, node):
        '''Helper function for in_order method.'''
        left = self.nodes[node].get('left')
        right = self.nodes[node].get('right')

        if left:
            for elem in self._in_order(left):
                yield elem
        yield node
        if right:
            for elem in self._in_order(right):
                yield elem

    def in_order(self):
        '''Return the values in the tree using in-order traversal.'''
        for elem in self._in_order(self.start):
            yield elem

    def _pre_order(self, node):
        '''Helper function for pre_order method.'''
        left = self.nodes[node].get('left')
        right = self.nodes[node].get('right')

        yield node
        if left:
            for elem in self._pre_order(left):
                yield elem
        if right:
            for elem in self._pre_order(right):
                yield elem

    def pre_order(self):
        '''Return the values in the tree using pre-order traversal.'''
        for elem in self._pre_order(self.start):
            yield elem

    def _post_order(self, node):
        '''Helper function for post_order method.'''
        left = self.nodes[node].get('left')
        right = self.nodes[node].get('right')

        if left:
            for elem in self._post_order(left):
                yield elem
        if right:
            for elem in self._post_order(right):
                yield elem
        yield node

    def post_order(self):
        '''Return the values in the tree using post-order traversal.'''
        for elem in self._post_order(self.start):
            yield elem

    def breadth_first(self):
        '''Return the values in the tree using breadth-first traversal.'''
        visited = []
        if self.start is None:
            return
        # yield self.start
        # visited.append(self.start)
        start_visited = visited
        while len(visited) < len(self.nodes):
            list_of_nodes_at_current_depth = []
            for node_ in start_visited:
                for k, v in self.nodes[node_].iteritems():
                    visited.append(v)
                    list_of_nodes_at_current_depth.append(v)
                    yield v
            start_visited = list_of_nodes_at_current_depth
            if len(list_of_nodes_at_current_depth) == 0:
                break




    # def breadth_first_traversal(self, start):
    #     """Perform a full breadth-first traversal of the graph beginning at start.
    #     Return the path when complete."""
    #     visited = []
    #     visited.append(start)
    #     start_visited = visited
    #     while True:
    #         temp = []
    #         for node_ in start_visited:
    #             for i in self.neighbors(node_):
    #                 if i not in visited:
    #                     visited.append(i)
    #                     temp.append(i)
    #         start_visited = temp
    #         if not temp:
    #             break
    #     return visited



if __name__ == '__main__':
    b = bst()
    b.insert(25)
    for i in range(1, 50):
        b.insert(i)

    b.print_dot()