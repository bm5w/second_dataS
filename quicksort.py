
class Quicksort(object):

    def __init__(self, input_list):
        if type(input_list) is not list:
            raise TypeError('Input type must be list.')
        self.input_list = input_list

    def swap(self, first, second):
        self.input_list[first], self.input_list[second] = self.input_list[second], self.input_list[first]

    def quicksort(self):
        self._quicksort(0, len(self.input_list)-1)
        return self.input_list

    def _find_pivot(self, start, finish):
        """Return index of median of start, finish, and middle values."""
        if (finish-start) <= 3:
            return finish
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

    def _quicksort(self, start, finish):
        """Recursive helper method for quicksort."""
        if finish > start:
            pivot_index = self._find_pivot(start, finish)
            pivot = self.input_list[pivot_index]
            center = start
            for index in xrange(start, finish):
                if self.input_list[index] <= pivot:
                    self.swap(index, center)
                    center += 1
            self.swap(center, finish)
            self._quicksort(start, center-1)
            self._quicksort(center, finish)
