import pytest
from merge import mergesort


def test_merge_simple():
    input = [1, 3, 2]
    assert mergesort(input) == [1, 2, 3]


def test_merge():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20]
    assert mergesort(input) == [17, 20, 26, 31, 44, 54, 55, 71, 93]


def test_merge_large():
    input = range(10000)
    assert mergesort(input) == range(10000)


def test_merge_big_floats():
    input = [x*0.01 for x in range(0, 100)]
    assert mergesort(input) == [x*0.01 for x in range(0, 100)]


def test_wrong_type():
    input = 'x'
    with pytest.raises(TypeError):
        mergesort(input)


def test_merge_big_reverse():
    input = range(10000)[::-1]
    assert mergesort(input) == range(10000)


def test_merge_big_increase_decrease():
    input = range(5000)+range(5000)[::-1]
    expected = range(5000)*2
    expected.sort()
    assert mergesort(input) == expected


def test_merge_duplicates():
    input = (range(100)+range(100))[::-1]
    expected = range(100)+range(100)
    expected.sort()
    assert mergesort(input) == expected


def test_merge_all_duplicates():
    input = [100]*20
    assert mergesort(input) == [100]*20


def test_merge_stable():
    foo1 = Stable(100, 'foo1')
    foo2 = Stable(100.0, 'foo2')
    foo3 = Stable(10, 'foo3')
    foo4 = Stable(1, 'foo4')
    input = [foo1, foo2, foo3, foo4]
    assert mergesort(input) == [foo4, foo3, foo1, foo2]


class Stable(object):
    """A class for testing stable characteristic of merge sort."""

    def __init__(self, num, name):
        self.num = num
        self.name = name

    def __cmp__(self, obj):
        if self.num == obj.num:
            return 0
        elif self.num > obj.num:
            return 1
        else:
            return -1

    def __str__(self):
        return str(self.num)
