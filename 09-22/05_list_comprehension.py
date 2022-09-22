"""
List comprehension:
    a.Using list comprehension create list av Fahrenheit from this Celsius= [0,10,20.1,34.5]
    b.Using Tuple comprehension create tuple of T_Fahrenhite fromthe same Celsius list in a.
    c.Time both code and compare result , do the same using memory_profile , what do u think?
"""

# Celsius to Fahrenheit formula = (C * 1.8) + 32

import memory_profiler
import timeit

Celsius = [0, 10, 20.1, 34.5]


@memory_profiler.profile
def list_farenheit_memory(c: list):
    return [i * 1.8 + 32 for i in Celsius]


@memory_profiler.profile
def tuple_farenheit_memory(c: list):
    return tuple(i * 1.8 + 32 for i in Celsius)


def list_farenheit(c: list):
    return [i * 1.8 + 32 for i in Celsius]


def tuple_farenheit(c: list):
    return tuple(i * 1.8 + 32 for i in Celsius)


list_farenheit_memory(Celsius)
tuple_farenheit_memory(Celsius)

print(timeit.timeit("list_farenheit(Celsius)", 'from __main__ import list_farenheit, Celsius'))
print(timeit.timeit("tuple_farenheit(Celsius)", 'from __main__ import tuple_farenheit, Celsius'))


# List comprehension is faster because we make the list at the same time as we do the arguments.
# Tuple creates the tuple first then runs the arguments.

# Result:
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     16     19.9 MiB     19.9 MiB           1   @memory_profiler.profile
#     17                                         def list_farenheit_memory(c: list):
#     18     19.9 MiB      0.0 MiB           7       return [i * 1.8 + 32 for i in Celsius]

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#    21     19.9 MiB     19.9 MiB           1   @memory_profiler.profile
#    22                                         def tuple_farenheit_memory(c: list):
#    23     19.9 MiB      0.0 MiB          11       return tuple(i * 1.8 + 32 for i in Celsius)

# 0.47448390000499785 -> list
# 0.6807741000084206 -> tuple
