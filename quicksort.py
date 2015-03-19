"""Methods for sorting a list using the quicksort method."""


def swap(input_list, first, second):
    """Swap first and second index values in inputted list."""
    input_list[first], input_list[second] = input_list[second], input_list[first]


def quicksort(input_list):
    """Sort list with quicksort. Return TypeError if input isn't list."""
    if type(input_list) is not list:
        raise TypeError('Input type must be list.')
    _quicksort(input_list, 0, len(input_list)-1)
    return input_list


def _find_pivot(input_list, start, finish):
    """Return index of median of start, finish, and middle values."""
    if (finish-start) <= 3:
        return finish
    a = input_list[start]
    b = input_list[((finish-start)/2)+start]
    c = input_list[finish]
    if a < b:
        if b < c:
            return ((finish-start)/2)+start
    else:
        if a < c:
            return start
    return finish


def _quicksort(input_list, start, finish):
    """Recursive helper method for quicksort."""
    if finish > start:
        pivot_index = _find_pivot(input_list, start, finish)
        pivot = input_list[pivot_index]
        center = start
        # find center, with all less than or equal on left.
        for index in xrange(start, finish):
            if input_list[index] <= pivot:
                swap(input_list, index, center)
                center += 1
        swap(input_list, center, finish)
        _quicksort(input_list, start, center-1)
        _quicksort(input_list, center, finish)

if __name__ == '__main__':
    import time

    lengths = [10, 100, 1000]
    times = []
    for x in lengths:
        start = time.time()
        output = quicksort(range(x))
        elapsed = time.time() - start
        times.append(elapsed)
    print 'Best case scenario:'
    for length, tim in zip(lengths, times):
        print 'a list of length {} was sorted in {}'.format(length, tim)
    diff = []
    for x in range(len(times)-2):
        diff.append(times[x+1]/times[x])
    average = reduce(lambda x, y: x+y, diff) / len(diff)
    print 'As length increases by 10, time increases by {}'.format(average)

    lengths = [10, 100, 998]
    times = []
    for x in lengths:
        start = time.time()
        output = quicksort(x*[1])
        elapsed = time.time() - start
        times.append(elapsed)
    print 'Worse case scenario:'
    for length, tim in zip(lengths, times):
        print 'a list of length {} was sorted in {}'.format(length, tim)
    diff = []
    for x in range(len(times)-2):
        diff.append(times[x+1]/times[x])
    average = reduce(lambda x, y: x+y, diff) / len(diff)
    print 'As length increases by 10, time increases by {}'.format(average)
