
# collatz iterator implementation

cdef class CollatzGenerator:
    cdef unsigned int high
    def __cinit__(self unsigned int high):
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
        if self.i < self.high:
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
