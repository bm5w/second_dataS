def radixsort(input):
    base = 10  # The number of buckets to use.

    # Declare the number of buckets to use and create them.
    buckets = [list() for _ in range(base)]

    # Segment the input list into appropriate buckets.
    for item in input:

        # For each item in the list, append it into a bucket.
        # To determine which bucket it should go into, divide the item
        # by the base of the dataset in use.
        # IE: 
        # - an item of value 1 % 10 --> bucket 1
        # - an item of value 5 % 10 --> bucket 5
        buckets[item % base].append(item)

    # Reassign the buckets into a single list.

if __name__ == "__main__":
    import time

    lengths = [10, 100, 1000]
    times = []

    for x in lengths:
        start = time.time()
        output = radixsort(range(x))
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
        output = radixsort(x*[1])
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
