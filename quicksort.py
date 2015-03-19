def quicksort(input_list, start=0, finish=-1):
    print input_list
    pivot = input_list[0]
    greater = 0
    equal = 0
    counter = 0
    item = 0
    if finish-start == 0:
        return

    def swap(first, second):
        input_list[first], input_list[second] = input_list[second], input_list[first]
        print input_list

    if finish == -1:
        finish = len(input_list)
    while counter < (finish-start):
        counter += 1
        if input_list[item+start] < pivot:     # LESS THAN
            item += 1
        elif input_list[item+start] == pivot:  # EQUAL TO
            if (item+start) == (finish-1-greater-equal):
                break
            swap(item+start, finish - 1 - equal - greater)
            equal += 1
        else:                # GREATER THAN
            if (item+start) == (finish-1-greater-equal):
                break
            # swap last equal and last unsorted item
            swap(finish-1-greater, finish-1-greater-equal-1)
            swap(item+start, finish - 1 - greater - 1)
            greater += 1

    # for x in xrange(equal):
    #     swap(finish-1-x, finish-1-greater-equal-x)

    if finish-start-greater-equal-start > 1:
        quicksort(input_list, start, finish - start - greater - equal)
        quicksort(input_list, finish - greater, finish)

    return input_list
