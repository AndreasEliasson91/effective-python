"""
Tuples Vs Lists:
    Create Tuple from 0-10 and list from 0-10 (not range) and time both operation, which is faster and why?
"""
import timeit


def create_tuple():
    _tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def create_list():
    _list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


t = timeit.repeat(stmt='create_tuple()', number=10_000, setup='from __main__ import create_tuple', repeat=30)
print(f'The Time of create tuple  : {sum(t)/len(t)}')

t = timeit.repeat(stmt='create_list()', number=10_000, setup='from __main__ import create_list', repeat=30)
print(f'The Time of create list  : {sum(t)/len(t)}')


# Tuples are stored in single block memory, and are immutable compared to lists that are stored in two blocks of memory
# and they are mutable so the objects in the list can change. So simply put, tuple is using less memory = faster.

