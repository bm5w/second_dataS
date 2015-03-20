def radixsort(input_list):
    """Sort list of integers and strings with radix sort algorithm."""
    if type(input_list[0]) is str:
        # for case when sorting string
        base = 256
        string = True
        place = 0
    else:
        string = False
        base = 10  # The number of buckets to use.
        place = 1  # IE, the 1's, 10's, or 100's place.
    hold = -1  # A placeholder

    complete = False
    while not complete:
        complete = True

        # Declare the number of buckets to use and create them.
        buckets = [list() for _ in xrange(base)]

        # Segment the input list into appropriate buckets.
        for item in input_list:
            if string:
                if place < len(item):
                    hold = ord(item[place])
                else:
                    hold = 0
            else:
                hold = item // place

            # For each item in the list, append it into a bucket.
            # To determine which bucket it should go into, divide the item
            # by the base of the dataset in use.
            # IE: 
            # - an item of value 1 % 10 --> bucket 1
            # - an item of value 5 % 10 --> bucket 5
            buckets[int((hold % base))].append(item)

            # Hold will be greater than 0 while there is a value in the list
            # that has a number in the decimal place that has not already been
            # iterated through.
            if string:
                if complete and hold > len(item):
                    complete = False
            else:
                if complete and hold > 0:
                    complete = False

        # Reassign the buckets into a single list.
        value = 0
        for bucketIndex in xrange(base):
            placeholder = buckets[bucketIndex]
            for item in placeholder:

                input_list[value] = item
                value += 1
        print input_list
        # Move on to the next decimal place
        # We start the loop at the 1's place, as declared in line 3,
        # do our sorting, and then multiply to place by the base, which brings
        # us to 10, the next decimal place to work with.
        # TLDR: 1 --> 10 --> 100, etc.
        if string:
            place += 1
        else:
            place *= base
    return input_list

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
