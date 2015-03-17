from collections import deque


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
