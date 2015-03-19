def quicksort(input, start=0, finish=0):

    pivot = input[0]
    greater = 0
    equal = 0
    counter = 0
    item = 0

    def swap(first, second):
        input[first], input[second] = input[second], input[first]

    if finish = 0:
        finish = len(input)

    while counter < len(input):
        counter += 1
        if item < pivot:     # LESS THAN
            item += 1
        elif item == pivot:  # EQUAL TO
            swap(item, len(input) - 1 - equal)
            equal += 1
        else:                # GREATER THAN
            swap(item, len(input - 1 - greater - equal))
            greater += 1


    left = quicksort(input, start, finish - start - greater - equal)
    right = quicksort(input, finish - greater, finish)

    return left + equal * [pivot] + right
