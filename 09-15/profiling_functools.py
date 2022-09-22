import functools
import profile


@functools.lru_cache(maxsize=None)
def fib_memorized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_memorized(n - 1) + fib_memorized(n - 2)


def fib_seq_memorized(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq_memorized(n - 1))
    seq.append(fib_memorized(n))
    return seq


profile.run('print(fib_seq_memorized(20)); print()')
profile.run('print(fib_memorized(20)); print()')
