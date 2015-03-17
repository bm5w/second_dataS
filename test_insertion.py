import pytest
from insertion import insertion


def test_insertion():
    input = [54,26,93,17,71,31,44,55,20]
    assert insertion(input) == [17,20,26,31,44,54,55,71,93]


def test_insertion_big():
    input = range(10000)
    assert insertion(input) == range(10000)


def test_wrong_type():
    input = 'x'
    with pytest.raises(TypeError):
        insertion(input)


def test_wrong_type_in_list():
    input = [1, 2, 'a']
    with pytest.raises(TypeError):
        insertion(input)


def test_insertion_big_reverse():
    input = range(10000)[::-1]
    assert insertion(input) == range(10000)