def radixsort(input):
    base = 10  # The number of buckets to use.
    place = 1  # IE, the 1's, 10's, or 100's place.

    complete = False
    while not complete:
        complete = True

        # Declare the number of buckets to use and create them.
        buckets = [list() for _ in range(base)]

        # Segment the input list into appropriate buckets.
        for item in input:
            hold = item / place

            # For each item in the list, append it into a bucket.
            # To determine which bucket it should go into, divide the item
            # by the base of the dataset in use.
            # IE: 
            # - an item of value 1 % 10 --> bucket 1
            # - an item of value 5 % 10 --> bucket 5
            buckets[hold % base].append(item)

        # Reassign the buckets into a single list.
        value = 0
        for bucketIndex in range(base):
            placeholder = buckets[bucketIndex]
            for item in placeholder:
                input[value] = item
                value += 1

        # Move on to the next decimal place
        # We start the loop at the 1's place, as declared in line 3,
        # do our sorting, and then multiply to place by the base, which brings
        # us to 10, the next decimal place to work with.
        # TLDR: 1 --> 10 --> 100, etc.
        place *= base

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
