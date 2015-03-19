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
    t = radixsort([1,2,3,4])
