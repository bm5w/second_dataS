import pytest
from quicksort import Quicksort


def test_quicksort_simple():
    input = [1, 3, 2]
    assert Quicksort(input).quicksort() == [1, 2, 3]


def test_quicksort():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20]

    assert Quicksort(input).quicksort() == [17, 20, 26, 31, 44, 54, 55, 71, 93]


def test_quicksort_duplicate():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20, 20]

    assert Quicksort(input).quicksort() == [17, 20, 20, 26, 31, 44, 54, 55, 71, 93]


def test_quicksort_duplicate():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20, 20, 20]

    assert Quicksort(input).quicksort() == [17, 20, 20, 20, 26, 31, 44, 54, 55, 71, 93]


def test_quicksort_large():
    input = range(1000)

    assert Quicksort(input).quicksort() == range(1000)


def test_quicksort_big_floats():
    input = [x*0.01 for x in range(0, 100)]

    assert Quicksort(input).quicksort() == [x*0.01 for x in range(0, 100)]


def test_wrong_type():
    input = 'x'
    with pytest.raises(TypeError):
        Quicksort(input).quicksort()


def test_quicksort_big_reverse():
    input = range(1000)[::-1]

    assert Quicksort(input).quicksort() == range(1000)


def test_quicksort_big_increase_decrease():
    input = range(500)+range(500)[::-1]
    expected = range(500)*2
    expected.sort()

    assert Quicksort(input).quicksort() == expected


def test_quicksort_duplicates():
    input = (range(100)+range(100))[::-1]
    expected = range(100)+range(100)
    expected.sort()

    assert Quicksort(input).quicksort() == expected


def test_quicksort_all_duplicates():
    input = [100]*20

    assert Quicksort(input).quicksort() == [100]*20
