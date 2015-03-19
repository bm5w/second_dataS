import pytest
from radix import radixsort


def test_radixsort_simple():
    input = [1, 3, 2]
    assert radixsort(input) == [1, 2, 3]


def test_radixsort():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20]

    assert radixsort(input) == [17, 20, 26, 31, 44, 54, 55, 71, 93]


def test_radixsort_duplicate():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20, 20]

    assert radixsort(input) == [17, 20, 20, 26, 31, 44, 54, 55, 71, 93]


def test_radixsort_more_duplicates():
    input = [54, 26, 93, 17, 71, 31, 44, 55, 20, 20, 20, 20]

    assert radixsort(input) == [17, 20, 20, 20, 20, 26, 31, 44, 54, 55, 71, 93]


def test_radixsort_large():
    input = range(10000)

    assert radixsort(input) == range(10000)


def test_wrong_type():
    input = 'x'
    with pytest.raises(TypeError):
        radixsort(input)


def test_radixsort_big_reverse():
    input = range(1000)[::-1]

    assert radixsort(input) == range(1000)


def test_radixsort_big_increase_decrease():
    input = range(500)+range(500)[::-1]
    expected = range(500)*2
    expected.sort()

    assert radixsort(input) == expected


def test_radixsort_duplicates():
    input = (range(100)+range(100))[::-1]
    expected = range(100)+range(100)
    expected.sort()

    assert radixsort(input) == expected


def test_radixsort_all_duplicates():
    input = [100]*20

    assert radixsort(input) == [100]*20


def test_radixsort_strings():
    input = ['c', 'b', 'a']

    assert radixsort(input) == ['a', 'b', 'c']

def test_radixsort_strings():
    input = ['chrit', 'boc', 'bob', 'chris']

    assert radixsort(input) == ['bob', 'boc', 'chris', 'chrit']
