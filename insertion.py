import time


def timed_func(func):
    """Decorator for timing our traversal methods."""
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        # print "time expired: %s" % elapsed
        return (result, elapsed)
    return timed


@timed_func
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
    lengths = [10, 100, 1000, 10000]
    times = []
    for x in lengths:
        output = insertion(range(x))
        times.append(output[1])
    print 'Best case scenario:'
    for length, tim in zip(lengths, times):
        print 'a list of length {} was sorted in {}'.format(length, tim)
    diff = []
    for x in range(len(times)-2):
        diff.append(times[x+1]/times[x])
    average = reduce(lambda x, y: x+y, diff) / len(diff)
    print 'As length increases by 10, time increases by {}'.format(average)

    lengths = [10, 100, 1000, 10000]
    times = []
    for x in lengths:
        output = insertion(range(x)[::-1])
        times.append(output[1])
    print 'Worse case scenario:'
    for length, tim in zip(lengths, times):
        print 'a list of length {} was sorted in {}'.format(length, tim)
    diff = []
    for x in range(len(times)-2):
        diff.append(times[x+1]/times[x])
    average = reduce(lambda x, y: x+y, diff) / len(diff)
    print 'As length increases by 10, time increases by {}'.format(average)


