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
                self.nodes[val] = {'parent': node}

            else:
                self._insert(self.nodes[node]['right'], val)
        else:
            if self.nodes[node].get('left') is None:
                self.nodes[node]['left'] = val
                self.nodes[val] = {'parent': node}
            else:
                self._insert(self.nodes[node]['left'], val)

    def insert(self, val):
        '''Insert a value into the bst unless already present.'''
        if self.contains(val):
            return None
        if self.start is None:
            self.start = val
            self.nodes[val] = {}
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
        if not node:
            return
        for elem in self._in_order(self.nodes[node].get('left', [])):
            yield elem
        yield node
        for elem in self._in_order(self.nodes[node].get('right', [])):
            yield elem

    def in_order(self):
        '''Return the values in the tree using in-order traversal.'''
        for elem in self._in_order(self.start):
            yield elem

    def _pre_order(self, node):
        '''Helper function for pre_order method.'''
        if not node:
            return
        yield node
        for elem in self._pre_order(self.nodes[node].get('left', [])):
            yield elem
        for elem in self._pre_order(self.nodes[node].get('right', [])):
            yield elem

    def pre_order(self):
        '''Return the values in the tree using pre-order traversal.'''
        for elem in self._pre_order(self.start):
            yield elem

    def _post_order(self, node):
        '''Helper function for post_order method.'''
        if not node:
            return
        for elem in self._post_order(self.nodes[node].get('left', [])):
            yield elem
        for elem in self._post_order(self.nodes[node].get('right', [])):
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
        visited.append(self.start)
        start_visited = [self.start]
        while len(visited) < len(self.nodes):
            list_of_nodes_at_next_depth = []
            for node_ in start_visited:
                visited.append(node_)
                if self.nodes[node_].get('left'):
                    list_of_nodes_at_next_depth.append(self.nodes[node_].get('left'))
                if self.nodes[node_].get('right'):
                    list_of_nodes_at_next_depth.append(self.nodes[node_].get('right'))
                yield node_
            start_visited = list_of_nodes_at_next_depth
            if len(list_of_nodes_at_next_depth) == 0:
                break

    def delete(self, val):
        '''Remove val from the tree if present, return None in all cases.'''
        if val not in self.nodes:
            return
        # No children
        elif self.nodes[val].get('left') is None and self.nodes[val].get('right') is None:
            del self.nodes[val]
            self._change_ref(val)
        # Single child
        elif self.nodes[val].get('left') is None or self.nodes[val].get('right') is None:
            del self.nodes[val]
            self._change_ref(val)
        else:
            pass

    def _change_ref(self, val, new_node=None):
        '''Delete link to specific node.'''
        for key, value in self.nodes.iteritems():
            if value.get('left') == val:
                value['left'] = new_node
                break
            if value.get('right') == val:
                value['right'] = new_node
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
    b.start = 5
    b.nodes = {
       5:{'left': 4, 'right': 10},
       4:{'left': 3, 'right': None, 'parent': 5},
       10:{'left': 7, 'right': 11, 'parent': 5},
       7:{'left': 6, 'right': None, 'parent': 10},
       6:{'left': None, 'right': None, 'parent': 7},
       11:{'left': None, 'right': None, 'parent': 10},
       3:{'left': 2, 'right': None, 'parent': 4},
       2:{'left': None, 'right': None, 'parent': 3}
    }

    b.print_dot()
