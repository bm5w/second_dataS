import timeit

def insertion(_list):
    '''Sorts a list via the insertion method.'''
    if type(_list) is not list:
        raise TypeError('Entire list must be numbers')
    for i in range(1, len(_list)):

        key = _list[i]
        if not isinstance(key, int):
            raise TypeError('Entire list must be numbers')
        position = i

        while position > 0 and _list[position-1] > key:
            _list[position] = _list[position-1]
            position = position-1

        _list[position] = key

    return _list

if __name__ == '__main__':
    input = [1, 3, 2]
    output = insertion(input)
    print output

    timeit.timeit(insertion(input))
