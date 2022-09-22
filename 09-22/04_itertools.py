"""
Itertools:
    a.Please Check the documentation of itertools here then:
    b.Create function string_perm_list(my_string)
      that return list of all possible order of the input string“ABCD”
      so the output like:(hint here)
      ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC'...]
    c.Now create same function but it returns tuple string_prem_tuple(my_string).
    d.Use input_test_string= “0123456789”and check timing, and memory_profile for both the list and tuple version.
    e.What do think about results of both in d?
"""
import itertools
import memory_profiler
import timeit


@memory_profiler.profile
def string_perm_list_memory(my_string: str) -> list[str]:
    return [''.join(i) for i in itertools.permutations(my_string, len(my_string))]


@memory_profiler.profile
def string_perm_tuple_memory(my_string: str) -> tuple[str]:
    return tuple(''.join(i) for i in itertools.permutations(my_string, len(my_string)))


def string_perm_list(my_string: str) -> list[str]:
    return [''.join(i) for i in itertools.permutations(my_string, len(my_string))]


def string_perm_tuple(my_string: str) -> tuple[str]:
    return tuple(''.join(i) for i in itertools.permutations(my_string, len(my_string)))


print(string_perm_list('ABCD'))
print(string_perm_tuple('ABCD'))


input_test_string = '0123456789'

string_perm_tuple_memory(input_test_string)
string_perm_list_memory(input_test_string)

print(timeit.timeit(stmt='string_perm_list(input_test_string)',
                    setup='from __main__ import string_perm_list, input_test_string',
                    number=10
                    ))
print(timeit.timeit(stmt='string_perm_tuple(input_test_string)',
                    setup='from __main__ import string_perm_tuple, input_test_string',
                    number=10
                    ))

# Result:
# list vs. tuple -> 6.931156499999815 sec : 7.552724400000443 sec
# List goes faster becuase you can use list comprehension.

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     17     19.9 MiB     19.9 MiB           1   @memory_profiler.profile
#     18                                         def string_perm_list_memory(my_string: str) -> list[str]:
#     19    270.3 MiB   -414.7 MiB     3628803       return [''.join(i) for i in itertools.permutations(my_string, len(my_string))]
#
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     22     21.1 MiB     21.1 MiB           1   @memory_profiler.profile
#     23                                         def string_perm_tuple_memory(my_string: str) -> tuple[str]:
#     24    273.6 MiB   -725.6 MiB     7257603       return tuple(''.join(i) for i in itertools.permutations(my_string, len(my_string)))
