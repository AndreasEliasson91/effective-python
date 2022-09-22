"""
List Generators:
    a.Create a function power2(n)that return list of power 2(like3**2) of list from 0-(n-1)?
    b.Then create a function power2_generator(n)that do the same thing as power2(n) but as generator!
    c.Write needed code to print the list elements in both cases!
    d.Check timeit and memoryprofile for both functions power2(n)and power2_generator(n)for n=10000.
"""
import timeit
import memory_profiler


@memory_profiler.profile
def power2_memory(n: int) -> list[int]:
    return [i**2 for i in range(n-1)]


@memory_profiler.profile
def power2_generator_memory(n: int):
    _generator = (i**2 for i in range(n-1))

    try:
        while True:
            item = next(_generator)
    except StopIteration:
        pass
    finally:
        print('Done!')
        

def power2(n: int) -> list[int]:
    return [i**2 for i in range(n-1)]


def power2_generator(n: int):
    for i in range(n-1):
        yield i**2


def print_func(n: int) -> None:
    print(power2(n))
    print(list(power2_generator(n)))


power2_memory(10000)
power2_generator_memory(10000)

print(timeit.timeit("power2(10000)", 'from __main__ import power2'))
print(timeit.timeit("power2_generator(10000)", 'from __main__ import power2_generator'))


# Results:

# This time is from 10 iterations, 10000 would take forever. But results would be similar.
# 2.0749451000010595 -> power 2
# 0.155330799985677 -> power2_generator

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     12     19.9 MiB     19.9 MiB           1   @memory_profiler.profile
#     13                                         def power2_memory(n: int) -> list[int]:
#     14     19.9 MiB      0.0 MiB        1002       return [i**2 for i in range(n-1)]

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     17     19.9 MiB     19.9 MiB           1   @memory_profiler.profile
#     18                                         def power2_generator_memory(n: int):
#     19     19.9 MiB      0.0 MiB       20001       _generator = (i**2 for i in range(n-1))
#     20
#     21     19.9 MiB      0.0 MiB           1       try:
#     22     19.9 MiB      0.0 MiB       10000           while True:
#     23     19.9 MiB      0.0 MiB       10000               item = next(_generator)
#     24     19.9 MiB      0.0 MiB           1       except StopIteration:
#     25     19.9 MiB      0.0 MiB           1           pass
#     26                                             finally:
#     27     19.9 MiB      0.0 MiB           1           print('Done!')
