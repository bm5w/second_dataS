def insertion(list):
    '''Sorts a list via the insertion method.'''

    for i in range(1, len(list)):

        key = list[i]
        position = i

        while position > 0 and list[position-1] > key:
            list[position] = list[position-1]
            position -= 1

        list[position] = key
