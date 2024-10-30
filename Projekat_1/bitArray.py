import itertools


class bitArray:
    def __init__(self, iterable):
        self.arr = list(map(bool, iterable))
    
    def __iter__(self):
        return iter(self._arr)
    
    def tobytes(self):
        return bytes(sum((bit << 1 for (i,bit) in enumerate(batch)),0)
                     for batch in itertools.batched(self._arr,8))
    