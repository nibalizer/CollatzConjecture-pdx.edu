# Use a very fast iterator that calculates values in C instead of pre
# calculating and storing in memory. Matplotlib can directly use this
# iterator when combined with xrange(high)
# 
# plot(xrange(2, high + 1), CollatzGenerator(high))
# 
# Requires: Cython, python headers (sometimes in python-dev package)
# Cython does not currently support generators, so manually write the
# classes

cdef class CollatzGenerator:
    cdef unsigned int high
    def __cinit__(self, unsigned int high):
        assert high > 2
        self.high = high

    def __iter__(self):
        return CollatzIterator(self.high)


cdef class CollatzIterator:
    cdef unsigned int i, high

    # cinit is for working directly with the struct
    def __cinit__(self, unsigned int high):
        self.i = 2
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        cdef unsigned int n, length
        if self.i > self.high:
            raise StopIteration
        n = self.i
        length = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            length += 1
        self.i += 1
        return length

cdef class CollatzEnumIterator(CollatzIterator):
    def __next__(self):
        cdef unsigned int length, i
        i = self.i # keep i before running __next__
        length = CollatzIterator.__next__(self)
        return (i, length)

cdef class CollatzEnumGenerator(CollatzGenerator):
    def __iter__(self):
        return CollatzEnumIterator(self.high)