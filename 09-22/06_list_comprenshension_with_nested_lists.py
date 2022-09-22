"""
List comprehension with nested lists:
    a.Using generator. Let’s create my_nest_list that has 3 numbers
      of list from 0-4 ,5-9 and 10-14. output:[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
    b.Using list comprehension create a list of double value of even numbers in my_nest_list.
      output:[[0, 4, 8], [12, 16], [20, 24, 28]]
    c.Using list comprehension create a list of double value of even numbers in my_list also the number itself if
      it was odds in the same order.output :[[0, 1, 4, 3, 8], [5, 12, 7, 16, 9], [20, 11, 24, 13, 28]]
    d.Repeat a,b,c with tuples, then check if that faster  and , if that save a memory?
    e.Using list comprehension flat the nested list my_nest_list
    f.Using itertools /chain to flat the same list.
    g.Compare timing of both operation using time it , what do u think ?
"""
import itertools
import timeit
import memory_profiler


# a.
def separate_numbers(n: int):
    yield from range(n)


@memory_profiler.profile
def list_generator_memory():
    _lists = separate_numbers(15)

    _my_nested_lists = [[next(_lists) for _ in range(5)] for _ in range(3)]
    print(f'Nested Lists: {_my_nested_lists}')

    _double_even = [[value * 2 for value in lis if value % 2 == 0] for lis in _my_nested_lists]
    print(f'Double Even Lists: {_double_even}')

    _my_lists = [[i * 2 if i % 2 == 0 else i for i in x] for x in _my_nested_lists]
    print(f'Double Even Lists, but keep all numbers: {_my_lists}')


@memory_profiler.profile
def tuple_generator_memory():
    _tuples = separate_numbers(15)

    _my_nested_tuples = tuple(tuple(next(_tuples) for _ in range(5)) for _ in range(3))
    print(f'Nested Tuples: {_my_nested_tuples}')

    _double_even_tuples = tuple(tuple(value*2 for value in lis if value % 2 == 0) for lis in _my_nested_tuples)
    print(f'Double Even Tuples: {_double_even_tuples}')
    _my_tuples = tuple(tuple(i*2 if i % 2 == 0 else i for i in x) for x in _my_nested_tuples)

    print(f'Double Even Tuples, but keep all numbers: {_my_tuples}')


# a.
lists = separate_numbers(15)
my_nested_lists = [[next(lists) for _ in range(5)] for _ in range(3)]
print(f'Nested Lists: {my_nested_lists}')
print(timeit.timeit('my_nested_lists', 'from __main__ import my_nested_lists'))


# b.
double_even = [[value*2 for value in lis if value % 2 == 0] for lis in my_nested_lists]
print(f'Double Even Lists: {double_even}')
print(timeit.timeit('double_even', 'from __main__ import double_even'))

# c.
my_lists = [[i*2 if i % 2 == 0 else i for i in x] for x in my_nested_lists]
print(f'Double Even Lists, but keep all numbers: {my_lists}')
print(timeit.timeit('my_lists', 'from __main__ import my_lists'))

# d.
lists = separate_numbers(15)
my_nested_tuples = tuple(tuple(next(lists) for _ in range(5)) for _ in range(3))
print(f'Nested Tuples: {my_nested_tuples}')
print(timeit.timeit('my_nested_tuples', 'from __main__ import my_nested_tuples'))

double_even_tuples = tuple(tuple(value*2 for value in lis if value % 2 == 0) for lis in my_nested_lists)
print(f'Double Even Tuples: {double_even_tuples}')
print(timeit.timeit('double_even_tuples', 'from __main__ import double_even_tuples'))

my_tuples = tuple(tuple(i*2 if i % 2 == 0 else i for i in x) for x in my_nested_lists)
print(f'Double Even Tuples, but keep all numbers: {my_tuples}')
print(timeit.timeit('my_tuples', 'from __main__ import my_tuples'))

list_generator_memory()
tuple_generator_memory()

# e.
my_flat_list = [val for sublist in my_nested_lists for val in sublist]
print(f'Flat List using comprehension: {my_flat_list}')
print(timeit.timeit('my_flat_list', 'from __main__ import my_flat_list'))


# f.
chain_list = [i for i in itertools.chain(*my_nested_lists)]
print(f'Flat List using itertools.chain(): {chain_list}')
print(timeit.timeit('chain_list', 'from __main__ import chain_list'))


# Results:
# nested list vs tuples -> 0.011476200000288372 sec : 0.011211699999876146 sec
# double even list vs tuple -> 0.011355499999808671 sec : 0.011199399999895832 sec
# double even keep numbers list vs tuple -> 0.011344500000632252 sec : 0.011192099999789207 sec
# flat list comp vs chain flat list -> 0.011209000000235392 sec : 0.011186499999894295 sec
# The chain method is faster becuase it doesn't use memory or take any memory.
#
#
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     48     20.1 MiB     20.1 MiB           1   @memory_profiler.profile
#     49                                         def list_generator_memory():
#     50     20.1 MiB      0.0 MiB           1       lists = separate_numbers(15)
#     51
#     52     20.1 MiB      0.0 MiB          27       my_nested_lists = [[next(lists) for _ in range(5)] for _ in range(3)]
#     53     20.1 MiB      0.0 MiB           1       print(f'Nested Lists: {my_nested_lists}')
#     54
#     55     20.1 MiB      0.0 MiB          27       double_even = [[value * 2 for value in lis if value % 2 == 0] for lis in my_nested_lists]
#     56     20.1 MiB      0.0 MiB           1       print(f'Double Even Lists: {double_even}')
#     57
#     58     20.1 MiB      0.0 MiB          27       my_lists = [[i * 2 if i % 2 == 0 else i for i in x] for x in my_nested_lists]
#     59     20.1 MiB      0.0 MiB           1       print(f'Double Even Lists, but keep all numbers: {my_lists}')
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     62     20.1 MiB     20.1 MiB           1   @memory_profiler.profile
#     63                                         def tuple_generator_memory():
#     64     20.1 MiB      0.0 MiB           1       lists = separate_numbers(15)
#     65
#     66     20.1 MiB      0.0 MiB          45       my_nested_tuples = tuple(tuple(next(lists) for _ in range(5)) for _ in range(3))
#     67     20.1 MiB      0.0 MiB           1       print(my_nested_tuples)
#     68
#     69     20.1 MiB      0.0 MiB          38       double_even_tuple = tuple(tuple(value*2 for value in lis if value % 2 == 0) for lis in my_nested_lists)
#     70     20.1 MiB      0.0 MiB           1       print(double_even_tuple)
#     71     20.1 MiB      0.0 MiB          45       my_tuples = tuple(tuple(i*2 if i % 2 == 0 else i for i in x) for x in my_nested_lists)
#     72
#     73     20.1 MiB      0.0 MiB           1       print(my_tuples)
