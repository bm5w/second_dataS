import pytest
from bst import bst


@pytest.fixture(scope='function')
def unbalanced():
    b = bst()
    b.start = 5
    b.nodes = {
       5:{'left': 2, 'right': 10},
       2:{'left': None, 'right': None},
       10:{'left': 7, 'right': 11},
       7:{'left': 6, 'right': None},
       6:{'left': None, 'right': None},
       11:{'left': None, 'right': None}
    }
    return b


@pytest.fixture(scope='function')
def balanced():
    b = bst()
    b.start = 5
    b.nodes = {
       5:{'left': 4, 'right': 10},
       4:{'left': 3, 'right': None},
       10:{'left': 7, 'right': 11},
       7:{'left': 6, 'right': None},
       6:{'left': None, 'right': None},
       11:{'left': None, 'right': None},
       3:{'left': 2, 'right': None},
       2:{'left': None, 'right': None}
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
    for expected, actual in zip(expected, balanced.in_order()):
        assert expected == actual













