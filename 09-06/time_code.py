import time


def old_fashion(n: int) -> list[str]:
    """
    Creates a list of integers from 0 to n and converts them to string
    :param n: int, number of integers
    :return: list[str], list of strings from integers
    """
    i = 0
    result = []
    while i < n:
        result.append(str(i))
        i += 1

    return result


def comprehension(n: int) -> list[str]:
    """
    Creates a list of integers from 0 to n and converts them to string
    :param n: int, number of integers
    :return: list[str], list of strings from integers
    """
    return [str(i) for i in range(n)]


def modern(n: int) -> list[str]:
    """
    Creates a list of integers from 0 to n and converts them to string
    :param n: int, number of integers
    :return: list[str], list of strings from integers
    """
    return list(map(str, range(n)))


start = time.perf_counter()
old_fashion(10_000_000)
print(f'Time: {time.perf_counter() - start : 0.4f}')

start = time.perf_counter()
comprehension(10_000_000)
print(f'Time: {time.perf_counter() - start : 0.4f}')

start = time.perf_counter()
modern(10_000_000)
print(f'Time: {time.perf_counter() - start : 0.4f}')
