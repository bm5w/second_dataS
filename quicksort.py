
class Quicksort(object):

    def __init__(self, input_list):
        if type(input_list) is not list:
            raise TypeError('Input type must be list.')

        self.input_list = input_list

    def swap(self, first, second):
        self.input_list[first], self.input_list[second] = self.input_list[second], self.input_list[first]
        print 'swap {}'.format(self.input_list)

    def quicksort(self):
        self._quicksort(0, len(self.input_list)-1)
        return self.input_list

    def _find_pivot(self, start, finish):
        """Return index of median of start, finish, and middle values."""
        a = self.input_list[start]
        b = self.input_list[((finish-start)/2)+start]
        c = self.input_list[finish]

        if a < b:
            if b < c:
                return ((finish-start)/2)+start
        else:
            if a < c:
                return start
        return finish
        return start

    def _quicksort(self, start, finish):
        print self.input_list
        if 2 > finish-start:
            return
        pivot_index = self._find_pivot(start, finish)
        self.swap(pivot_index, finish)
        pivot = self.input_list[finish]
        center = start
        index = start
        count = 0
        gt_or_eq = 0

        while count <= (finish-start):
            if self.input_list[index] < pivot:     # LESS THAN
                center += 1
                index += 1
            else:                                     # GREATER THAN or EQUAL
                self.swap(index, finish-gt_or_eq)
                gt_or_eq += 1
            count += 1

        self._quicksort(start, center)
        self._quicksort(center, finish)