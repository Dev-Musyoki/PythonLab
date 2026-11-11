# An iterator is an object that implements the iterator protocol, which consists of the methods__iter__() and __next__(). An iterable is an object that can return an iterator, which is done by implementing the __iter__() method.
# The for loop is built on one protocol. Python calls iter() on the collection, then calls next() repeatedly until it raises StopIteration.
# The for loop uses the iterator protocol automatically. 

# Iterator Vs Iterable:
# An iterable is an object you can loop over(like a list, tuple, set, dictionary, or string).
# An iterator is an object that remembers where it currently is during iteration and can give you the next value when requested. 
# __iter__() takes an iterable and returns an iterator.
# __next__() returns the next value from the iterator. Whhen there are no more items, it raises StopIteration.
# StopIteration is a special exception that tells Python there are no more items to iterate over. The loop catches this exception and stops the iteration.


stages = ["CBD", "Westlands", "Kangemi"]
it = iter(stages)
print(next(it))   # CBD
print(next(it))   # Westlands
print(next(it))   # Kangemi
# next(it) again would raise StopIteration

# Build your own iterator: an object with __iter__ and __next__
class StageIterator:
    def __init__(self, stages):
        self.stages = stages
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.stages):
            raise StopIteration
        stage = self.stages[self.index]
        self.index += 1
        return stage

for stage in StageIterator(["CBD", "Westlands", "Kangemi"]):
    print(stage)
# CBD
# Westlands
# Kangemi
