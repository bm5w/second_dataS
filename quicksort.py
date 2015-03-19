# def quicksort(input_list, start=0, finish=-1):
#     print input_list
#     pivot = input_list[0]
#     greater = 0
#     equal = 0
#     counter = 0
#     item = 0
#     if finish-start == 0:
#         return

#     def swap(first, second):
#         input_list[first], input_list[second] = input_list[second], input_list[first]
#         print input_list

#     if finish == -1:
#         finish = len(input_list)
#     while counter < (finish-start):
#         counter += 1
#         if input_list[item+start] < pivot:     # LESS THAN

#             item += 1
#         elif input_list[item+start] == pivot:  # EQUAL TO
#             if (item+start) == (finish-1-greater-equal):
#                 break
#             swap(item+start, finish - 1 - equal - greater)
#             equal += 1
#         else:                # GREATER THAN
#             if (item+start) == (finish-1-greater-equal):
#                 break
#             # swap last equal and last unsorted item
#             swap(finish-1-greater, finish-1-greater-equal-1)
#             swap(item+start, finish - 1 - greater - 1)
#             greater += 1

#     # for x in xrange(equal):
#     #     swap(finish-1-x, finish-1-greater-equal-x)

#     if finish-start-greater-equal-start > 1:
#         quicksort(input_list, start, finish - start - greater - equal)
#         quicksort(input_list, finish - greater, finish)

#     return input_list

# import sys
# sys.setrecursionlimit(1000)

# def quicksort(list_input):
#     g = []
#     l = []
#     # e = []

#     # if list_input == []:
#     #     return []

#     def swap(first, second):
#         list_input[first], list_input[second] = list_input[second], list_input[first]
#         print list_input

#     if len(list_input) < 2:
#         return list_input

#     pivot = list_input[len(list_input)//2]
#     swap(len(list_input)//2, 0)


#     for item in list_input[1:]:
#         if item >= pivot:
#             g.append(item)
#         # if item == pivot:
#         #     e.append(item)
#         if item < pivot:
#             l.append(item)

#     left = quicksort(l)
#     right = quicksort(g)

#     return left + [pivot] + right

def quicksort(input_list, start=0, finish=-1):
    print 'list: {} start: {} finish: {}'.format(input_list, start, finish)
    def swap(first, second):
        input_list[first], input_list[second] = input_list[second], input_list[first]
        print 'swap {}'.format(input_list)
    # import pdb; pdb.set_trace()
    if finish == -1:
        finish = len(input_list)-1

    if 2 > finish-start:
        return

    pivot = input_list[start]
    swap(start, finish)
    center = start
    index = start
    count = 0
    gt_or_eq = 0

    while count <= (finish-start):
        if input_list[index] < pivot:     # LESS THAN
            center += 1
            index += 1
        else:                                     # GREATER THAN or EQUAL
            swap(index, finish-gt_or_eq)
            gt_or_eq += 1
        count += 1

    quicksort(input_list, start, center)
    quicksort(input_list, center, finish)

    return input_list

