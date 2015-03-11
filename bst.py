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

    def left(self, node):
        return self.nodes[node].get('left')

    def right(self, node):
        return self.nodes[node].get('right')


    def delete(self, val):
        '''Remove val from the tree if present, return None in all cases.'''
        print 'value: {}\nleft: {}\nright: {}'.format(val, self.nodes[val].get('left'), self.nodes[val].get('right'))
        print 'self.start: {}'.format(self.start)
        if val not in self.nodes:
            return
        # No children
        elif self.nodes[val].get('left') is None and self.nodes[val].get('right') is None:
            if self.size() == 1:
                self.start = None
                del self.nodes[val]
            else:
                self._change_ref(val)
                del self.nodes[val]
            return
        # Single child
        left = self.nodes[val].get('left')
        right = self.nodes[val].get('right')
        # The case where only a right child exists.
        if left is None:
            self._change_ref(val, right)
            del self.nodes[val]
        elif right is None:
            self._change_ref(val, left)
            del self.nodes[val]
        # 3rd
        elif val > self.start:  # on right side of tree
            temp = self.nodes[left]
            self._change_ref(val, left)

            self.nodes[left]['right'] = self.nodes[val]['right']
            self.nodes[right]['parent'] = left

            self.nodes[val]['left'] = temp.get('left')
            self.nodes[val]['right'] = temp.get('right')
            self.nodes[val]['parent'] = left
            self.delete(val)
        elif val < self.start:  # on left side of tree
            temp = self.nodes[right]
            self._change_ref(val, right)

            self.nodes[right]['left'] = self.nodes[val]['left']
            self.nodes[left]['parent'] = right

            self.nodes[val]['right'] = temp.get('right')
            self.nodes[val]['left'] = temp.get('left')
            self.nodes[val]['parent'] = right
            self.delete(val)
        elif val == self.start:
            switch_to = self.highest_val(val)
            print 'highest_val: {}'.format(switch_to)
            self.start = switch_to
            self.switch_nodes(val, switch_to)
            self.delete(val)



            # temp_left = self.nodes[left]['left']
            # temp_right = self.nodes[left]['right']

            # self.start = left
            # self.nodes[self.start]['left'] = val
            # self.nodes[self.start]['right'] = right
            # self.nodes[self.start]['parent'] = None
            # self.nodes[val]['left'] = temp_left
            # self.nodes[val]['right'] = temp_right
            # self.nodes[val]['parent'] = self.start
            # self.delete(val)

    def highest_val(self, val):
        '''Return highest value that is less than val.'''
        ordered_list = sorted(self.nodes.keys())
        return ordered_list[ordered_list.index(val)-1]

    def switch_nodes(self, four, eleven):
        '''Switch references on two different nodes, effectively switching the nodes.'''
        temp = self.nodes[four]
        temp_left = temp.get('left')
        temp_right = temp.get('right')
        temp_parent = temp.get('parent')

        four_left = self.nodes[eleven].get('left')
        four_right = self.nodes[eleven].get('right')
        four_parent = self.nodes[eleven].get('parent')

        if four_left:
            self.nodes[four]['left'] = self.nodes[eleven].get('left')
        if four_right:
            self.nodes[four]['right'] = self.nodes[eleven].get('right')
        if four_parent:
            self.nodes[four]['parent'] = self.nodes[eleven].get('parent')

        if temp_left:
            self.nodes[eleven]['left'] = temp.get('left')
        if temp_right:
            self.nodes[eleven]['right'] = temp.get('right')
        if temp_parent:
            self.nodes[eleven]['parent'] = temp.get('parent')



    def _change_ref(self, val, new_node=None):
        '''Delete link to specific node.'''
        # TODO: What to do if single node
        temp_parent = self.nodes[val].get('parent')
        if temp_parent is None:
            self.start = new_node
            temp = self.nodes[new_node]
            self.nodes[new_node]['left'] = self.nodes[val].get('left')
            self.nodes[new_node]['right'] = val
            self.nodes[val]['right'] = temp.get('right')
            self.nodes[val]['left'] = temp.get('left')
            self.nodes[val]['parent'] = new_node
            return
        if self.nodes[temp_parent].get('left') == val:
            self.nodes[temp_parent]['left'] = new_node
        if self.nodes[temp_parent].get('right') == val:
            self.nodes[temp_parent]['right'] = new_node

    def jiggle(self, list):
        '''Rebalance the tree.'''

        # 1. Sort the tree into an ordered list
        # 2. Identify the midpoint of the list, and insert it to the graph.
        # 3. Split the list from the midpoint.
        # 4. Repeat step 2.
        if len(list) == 0:
            return
        print 'list: {}'.format(list)
        sorted_list = sorted(list)
        midpoint = len(sorted_list)/2
        if midpoint == 0:
            self.insert(sorted_list[0])
        else: 
            self.insert(sorted_list[midpoint])
            self.jiggle(sorted_list[:midpoint])
            self.jiggle(sorted_list[midpoint + 1:])

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
    b.jiggle(range(100))

    b.print_dot()
