"""
Iter Object:
    a.Converting datatypes like string to iter object is very useful.
       Read documentation about iter() and next() here and then answer these questions:
    b.Let’s say my_string = “I’m not iterator object” try command next(my_string) what you get?
    c.Create function that convert a string to iterator and print each character in single line using next().
"""

my_string = "I'm not iterator object"

# Receives TypeError: 'str' object is not an iterator
# print(next(my_string))


def str_to_iter(s: str) -> None:
    for _ in range(len(s)):
        s = iter(s)
        print(next(s))


str_to_iter(my_string)
