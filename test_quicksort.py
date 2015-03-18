import pytest
from quicksort import quicksort


def test_quicksort_simple():
    input = [1, 3, 2]
    assert quicksort(input) == [1, 2, 3]


def test_quicksort():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20]
    assert quicksort(input) == [17, 20, 26, 31, 44, 54, 55, 71, 93]


def test_quicksort_large():
    input = range(10000)
    assert quicksort(input) == range(10000)


def test_quicksort_big_floats():
    input = [x*0.01 for x in range(0, 100)]
    assert quicksort(input) == [x*0.01 for x in range(0, 100)]


def test_wrong_type():
    input = 'x'
    with pytest.raises(TypeError):
        quicksort(input)


def test_quicksort_big_reverse():
    input = range(10000)[::-1]
    assert quicksort(input) == range(10000)


def test_quicksort_big_increase_decrease():
    input = range(5000)+range(5000)[::-1]
    expected = range(5000)*2
    expected.sort()
    assert quicksort(input) == expected


def test_quicksort_duplicates():
    input = (range(100)+range(100))[::-1]
    expected = range(100)+range(100)
    expected.sort()
    assert quicksort(input) == expected


def test_quicksort_all_duplicates():
    input = [100]*20
    assert quicksort(input) == [100]*20
