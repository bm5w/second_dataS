class HashTable(object):
    '''An implementation of a hash table.'''

    def __init__(self, size=1024):
        '''Initialize a Hashtable of a given size.'''
        self.table = [[] for x in range(size)]
        self.size = size

    def hash(self, key):
        '''Hash the key provided.
        Key must be string, else TypeError is raised.'''
        val = 0
        if type(key) is not str:
            raise TypeError('Key must be a string.')
        for character in key:
            val += ord(character)
        return val % self.size

    def set(self, key, val):
        '''Store the given val using the given key.'''
        try:
            hashed_key = self.hash(key)
        except (NameError, TypeError):
            raise TypeError("Must use a string")

        for index, _tuple in enumerate(self.table[hashed_key]):
            if _tuple[0] == key:
                self.table[hashed_key][index] = (key, val)
                break
        else:
            self.table[hashed_key].append((key, val))

    def get(self, key):
        '''Return the value stored with the given key.'''
        for entries in self.table[self.hash(key)]:
            if key == entries[0]:
                return entries[1]
        raise KeyError('Key not found.')
