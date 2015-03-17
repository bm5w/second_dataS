import time
from collections import deque


def timed_func(func):
    """Decorator for timing our traversal methods."""
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        return (result, elapsed)
    return timed


@timed_func
def mergesort(input_list):
    """Sort list using mergesort methods.
    TypeError raised if not list. List must contain only numbers."""
    if type(input_list) is not list:
        raise TypeError('Entire list must be numbers')
    if len(input_list) > 1:
        center = len(input_list)/2
        left = deque(mergesort(input_list[:center]))
        right = deque(mergesort(input_list[center:]))
    else:
        return list(input_list)

    output = deque([])
    popA = left.popleft()
    popB = right.popleft()
    while True:
        if popA < popB:
            output.append(popA)
            if left:
                popA = left.popleft()
            else:
                output.append(popB)
                while right:
                    output.append(right.popleft())
                return list(output)
        else:
            output.append(popB)
            if right:
                popB = right.popleft()
            else:
                output.append(popA)
                while left:
                    output.append(left.popleft())
                return list(output)

if __name__ == '__main__':
    lengths = [10, 100, 1000, 10000, 100000, 1000000]
    times = []
    for x in lengths:
        output = mergesort(range(x))
        times.append(output[1])
    print 'Best case scenario:'
    for length, tim in zip(lengths, times):
        print 'a list of length {} was sorted in {}'.format(length, tim)
    diff = []
    for x in range(len(times)-2):
        diff.append(times[x+1]/times[x])
    average = reduce(lambda x, y: x+y, diff) / len(diff)
    print 'As length increases by 10, time increases by {}'.format(average)

    lengths = [10, 100, 1000, 10000, 100000, 1000000]
    times = []
    for x in lengths:
        output = mergesort(range(x)[::-1])
        times.append(output[1])
    print 'Worse case scenario:'
    for length, tim in zip(lengths, times):
        print 'a list of length {} was sorted in {}'.format(length, tim)
    diff = []
    for x in range(len(times)-2):
        diff.append(times[x+1]/times[x])
    average = reduce(lambda x, y: x+y, diff) / len(diff)
    print 'As length increases by 10, time increases by {}'.format(average)


