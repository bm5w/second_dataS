import pytest
from bst import bst


@pytest.fixture(scope='function')
def big_complex():
    '''A big complex binary tree with first node, 50.'''
    b = bst()
    b.insert(24)
    b.insert(11)
    b.insert(17)
    b.insert(20)

    b.insert(37)
    b.insert(43)
    b.insert(30)
    b.insert(48)
    b.insert(49)
    b.insert(11)
    b.insert(5)
    b.insert(2)
    b.insert(0)
    remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                 48, 49]
    for i in remaining:
        b.insert(i)
    return b

@pytest.fixture(scope='function')
def big():
    '''A big unbalanced binary tree with first node, 50.'''
    b = bst()
    b.insert(50)
    for i in range(50, 0, -1):
        b.insert(i)
    return b


@pytest.fixture(scope='function')
def big_balanced():
    '''A big balanced binary tree with first node, 50.'''
    b = bst()
    b.insert(25)
    for i in range(1, 50):
        b.insert(i)
    return b


@pytest.fixture(scope='function')
def unbalanced():
    b = bst()
    b.start = 5
    b.nodes = {
       5:{'left': 2, 'right': 10},
       2:{'left': None, 'right': None, 'parent': 5},
       10:{'left': 7, 'right': 11, 'parent': 5},
       7:{'left': 6, 'right': None, 'parent': 10},
       6:{'left': None, 'right': None, 'parent': 7},
       11:{'left': None, 'right': None, 'parent': 10}
    }

    return b


@pytest.fixture(scope='function')
def balanced():
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
    return b


@pytest.fixture(scope='function')
def empty():
    b = bst()
    b.nodes = {}
    return b


def test_init():
    '''Verify that the BST is instantiated as expected.'''
    b = bst()
    assert b.nodes == {}


def test_insert_empty(empty):
    '''Verify that a node can be inserted into an empty BST.'''
    empty.insert(4)
    assert empty.contains(4)


def test_insert_existing_into_populated(balanced):
    '''Verify that a node can be appropriately inserted into populated BST.'''
    before = balanced.size()
    balanced.insert(4)
    assert balanced.size() == before


def test_insert_unexisting_into_populated(unbalanced):
    '''Verify that a node can be appropriately inserted into populated BST.'''
    print unbalanced.nodes
    unbalanced.insert(8)
    print unbalanced.nodes
    assert unbalanced.nodes[7]['right'] == 8


def test_contains_true(unbalanced):
    '''Verify that existing nodes can be identified.'''
    assert unbalanced.contains(6)


def test_contains_false(unbalanced):
    '''Searches for nodes that do not exist should say so.'''
    assert not unbalanced.contains(1)


def test_size_empty(empty):
    '''Empty graphs should be identified as such.'''
    assert not empty.size()


def test_size_populated(unbalanced):
    '''Verify that the length of populated graphs are as expected.'''
    assert unbalanced.size() == 6


def test_depth_empty(empty):
    '''Empty graphs should have no depth.'''
    print 'dXXXXXXXXXX {}'.format(empty)
    assert not empty.depth()


def test_depth_populated_unbalanced(unbalanced):
    '''Verify that the depth of populated graphs are as expected.'''
    assert unbalanced.depth() == 4


def test_depth_populated_balanced(balanced):
    '''Verify that the depth of populated graphs are as expected.'''
    assert balanced.depth() == 4


def test_there_is_no_balance(empty):
    '''Empty graphs should be identified as such.'''
    assert not empty.balance()


def test_balanced(balanced):
    '''Balanced graphs should return 0.'''
    assert balanced.balance() == 0


def test_unbalanced_to_the_left(balanced):
    '''Graphs unbalanced to the left should return the appropriate positive value.'''
    balanced.insert(1)
    assert balanced.balance() > 0


def test_unbalanced_to_the_right(unbalanced):
    '''Graphs unbalanced to the right should return the appropriate negative value.'''
    assert unbalanced.balance() < 0


def test_in_order(balanced):
    '''Test generator in_order with balanced graph.'''
    expected = [2, 3, 4, 5, 6, 7, 10, 11]
    for expect, actual in zip(expected, balanced.in_order()):
        assert expect == actual


def test_in_order_big(big):
    '''Test generator in_order with big graph.'''
    expected = range(1, 51)
    for expect, actual in zip(expected, big.in_order()):
        assert expect == actual


def test_pre_order(balanced):
    '''Test generator pre_order with balanced graph.'''
    expected = [5, 4, 3, 2, 10, 7, 6, 11]
    for expect, actual in zip(expected, balanced.pre_order()):
        assert expect == actual


def test_pre_order_big(big):
    '''Test generator pre_order with balanced graph.'''
    expected = range(50, 0, -1)
    for expect, actual in zip(expected, big.pre_order()):
        assert expect == actual


def test_post_order(balanced):
    '''Test generator post_order with balanced graph.'''
    expected = [2, 3, 4, 6, 7, 11, 10, 5]
    for expect, actual in zip(expected, balanced.post_order()):
        assert expect == actual


def test_post_order_big(big):
    '''Test generator post_order with balanced graph.'''
    expected = range(1, 51)
    for expect, actual in zip(expected, big.post_order()):
        assert expect == actual


def test_breadth_first(balanced):
    '''Test generator breadth_first with balanced graph.'''
    expected = [5, 4, 10, 3, 7, 11, 2, 6]
    output = []
    for x in balanced.breadth_first():
        output.append(x)
    assert len(output) > 0
    for expect, actual in zip(expected, balanced.breadth_first()):
        assert expect == actual


def test_breadth_first_unbalanced(unbalanced):
    '''Test generator breadth_first with balanced graph.'''
    expected = [5, 2, 10, 7, 11, 6]
    output = []
    for x in unbalanced.breadth_first():
        output.append(x)
    assert len(output) > 0
    for expect, actual in zip(expected, unbalanced.breadth_first()):
        assert expect == actual


def test_breadth_first_big(big):
    '''Test generator breadth_first with big unbalanced graph.'''
    expected = range(50, 0, -1)
    output = []
    for x in big.breadth_first():
        output.append(x)
    assert len(output) > 0
    for expect, actual in zip(expected, big.breadth_first()):
        assert expect == actual


def test_breadth_first_big_balanced(big_balanced):
    '''Test generator breadth_first with big balanced graph.'''
    expected = [25, 1, 26, 2, 27, 3, 28, 4, 29, 5, 30, 6, 31, 7, 32, 8, 33, 9,
                34, 10, 35, 11, 36, 12, 37, 13, 38, 14, 39, 15, 40, 16, 41, 17,
                42, 18, 43, 19, 44, 20, 45, 21, 46, 22, 47, 23, 48, 24, 49]
    output = []
    for x in big_balanced.breadth_first():
        output.append(x)
    assert len(output) > 0
    for expect, actual in zip(expected, big_balanced.breadth_first()):
        assert expect == actual


def test_delete_no_descendents(balanced):
    balanced.delete(2)
    assert balanced.nodes[3]['left'] is None
    assert balanced.size() == 7


def test_delete_one_descendent(balanced):
    balanced.delete(3)
    assert balanced.nodes[4]['left'] == 2
    assert balanced.contains(3) is False


def test_delete_descendent_one_child(balanced):
    balanced.delete(4)
    assert balanced.nodes[5]['left'] == 3
    assert balanced.contains(4) is False


def test_delete_start_no_children(empty):
    empty.insert(10)
    empty.delete(10)
    assert empty.start is None
    assert empty.size() is 0


def test_delete_descendents_left_multiple_children(big_complex):
    big_complex.delete(43)
    assert big_complex.nodes[37]['right'] == 38
    assert big_complex.nodes[38]['right'] == 48
    assert big_complex.contains(43) is False


def test_delete_descendents_right_multiple_children(big_complex):
    big_complex.delete(17)
    assert big_complex.nodes[11]['right'] == 20
    assert big_complex.nodes[20]['right'] == 21

    assert big_complex.contains(17) is False


def test_delete_descendents_left_small_multiple_children(balanced):
    balanced.delete(10)
    assert balanced.nodes[5]['right'] == 7
    assert balanced.nodes[7]['right'] == 11
    assert balanced.contains(10) is False

def test_delete_descendents_multiple_children_top(balanced):
    balanced.delete(5)
    assert balanced.nodes[10]['right'] == 7
    assert balanced.nodes[10]['left'] == 4
    assert balanced.start == 10
