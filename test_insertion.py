import pytest
from insertion import insertion

def test_insertion():
    input = [54,26,93,17,71,31,44,55,20]
    assert insertion(input) == [17,20,26,31,44,54,55,71,93]
