import pytest
from hash import HashTable


@pytest.fixture(scope ='function')
def simple_HashTable():
    simple_ht = HashTable(2000)
    return simple_ht


def test_init(simple_HashTable):
    assert len(simple_HashTable.table) == 2000


def test_hash_with_single_character(simple_HashTable):
    assert simple_HashTable.hash('a') == 97


def test_hash_with_long_string(simple_HashTable):
    assert simple_HashTable.hash('abcdefghijklmnopqrstuvwxyz') == 847


def test_hash_with_long_string_num(simple_HashTable):
    assert simple_HashTable.hash('1234567890') == 525


def test_hash_with_long_num_string(simple_HashTable):
    assert simple_HashTable.hash('1234567890abcdefghijklmnopqrstuvwxyz') == 1372


def test_hash_non_string(simple_HashTable):
    with pytest.raises(TypeError):
        simple_HashTable.hash(12345)


def test_set(simple_HashTable):
    simple_HashTable.set('test', 'value')
    hash_value = simple_HashTable.hash('test')
    assert simple_HashTable.table[hash_value][0][1] == 'value'


def test_set_error(simple_HashTable):
    with pytest.raises(TypeError):
        simple_HashTable.set(1234, 'value')


def test_get(simple_HashTable):
    simple_HashTable.set('test', 'value')
    assert simple_HashTable.get('test') == 'value'


def test_buckets_are_not_same(simple_HashTable):
    simple_HashTable.set('test', 'value')
    index = simple_HashTable.hash('test')
    assert simple_HashTable.table[index] != simple_HashTable.table[index+1]


@pytest.fixture(scope='function')
def populated_HashTable():
    populated_HashTable = HashTable()
    length = 235886
    list_words = []
    with open('words') as f:
        for x in range(length):
            word = f.readline().rstrip('\n')
            populated_HashTable.set(str(word), str(word))
            list_words.append(word)
    return (populated_HashTable, list_words)


def test_populated(populated_HashTable):
    for item in populated_HashTable[1]:
        assert item == populated_HashTable[0].get(item)


def test_duplicate_key(simple_HashTable):
    simple_HashTable.set('test', 'value')
    length = simple_HashTable.table[simple_HashTable.hash('test')]
    simple_HashTable.set('test', 'value')
    length_end = simple_HashTable.table[simple_HashTable.hash('test')]
    assert length == length_end


def test_duplicate_key_overwrites(simple_HashTable):
    simple_HashTable.set('test', 'value')
    simple_HashTable.set('test', 'value2')
    assert simple_HashTable.get('test') == 'value2'

