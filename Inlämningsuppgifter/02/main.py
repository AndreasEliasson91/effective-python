class Demonstration:
    @staticmethod
    def demonstrate_list_of_string() -> None:
        from list_of_string import ListOfString

        data = ListOfString([11, 2, 22, 4, 105])

        # Print full list and __getitem__ at index 3
        print(f'List Of Strings: {data}')
        print(f'Element At Index 3: {data[3]}')

        # Append element
        data.append(192)
        print(f'List After append(192): {data}')

        # Extend elements from list
        data.extend([11, 1.0, True, 'A'])
        print(f'List After extend({[11, 1.0, True, "A"]}): {data}')

        # Insert elements at specific index
        data.insert(5, 5)
        print(f'List After insert(5, 5): {data}\n')

        # Use __add__, __iadd__ and __radd__ to add elements to the list
        data = data + ['x', 3, 99, 'Hoa', '7', 4]
        print(f'List After Adding ["x", 3, 99, "Hoa", "7", 4]): {data}')

        data += [11, 'A', 0, '17', 9, 44]
        print(f'List After += [11, "A", 0, "17", 9, 44]): {data}')

        data2 = ListOfString(['Nice!', 'New String', 123, False])
        print(f'New List Of Strings: {data2}')

        data += data2
        print(f'List After Reverse Add New ListOfStrings: {data}')

    @staticmethod
    def demonstrate_list_of_num() -> None:
        from list_of_num import ListOfNum

        my_numbers = ListOfNum([1.1, 2, 3j])
        # my_numbers = ListOfNum([1.1, 3j, 'X'])  # Raises TypeError
        print(my_numbers)

        # Append element
        my_numbers.append(1)
        # my_numbers.append('4.2')  # Raises TypeError
        print(my_numbers)

        # Extend elements from list
        my_numbers.extend([2.5, 3j, 8])
        # my_numbers.extend([1.1, '3j', 8.0])  # Raises TypeError
        print(my_numbers)

        # Insert elements at specific index
        my_numbers.insert(2, 99)
        # my_numbers.insert(2, '99')  # Raises TypeError
        print(my_numbers)

    @staticmethod
    def demonstrate_andreas_list() -> None:
        from andreas_list import AndreasList

        stmt = AndreasList(['Welcome', 2, 'Python,', 'Welcome', 'to', 'GÖT'])
        print(stmt)

        # Join it to string, without alterning with object
        print(stmt.join_it())

        # Map a function on each element
        print(stmt.map_it(str.upper))
        print(stmt.map_it(str.lower))

        # Filter list from predicate, before and after appending 'Post'
        print(stmt.filter_it(lambda item: item.startswith('P')))
        stmt.append('Post')
        print(stmt.filter_it(lambda item: item.startswith('P')))

        # Add function call for each item in list
        print(stmt.for_each_item(id))
        stmt.for_each_item(print)

    @staticmethod
    def demonstrate_timeit() -> None:
        import timeit

        # Output: 184.33774470000026
        _import = 'from list_of_string import ListOfString'
        test_code = 'list_of_string = ListOfString([]);list_of_string.extend([i for i in range(100_000)])'
        print('Time For ListOfString:', end=' ')
        print(timeit.timeit(stmt=test_code, setup=_import, number=10_000))

        # Output: 181.6198072999996
        _import = 'from list_of_user_string import ListOfUserString'
        test_code = 'list_of_user_string = ListOfUserString([]);list_of_user_string.extend([i for i in range(100_000)])'
        print('Time For ListOfUserString:', end=' ')
        print(timeit.timeit(stmt=test_code, setup=_import, number=10_000))


def main():
    demonstration = Demonstration()

    demonstration.demonstrate_list_of_string()
    demonstration.demonstrate_list_of_num()
    demonstration.demonstrate_andreas_list()
    demonstration.demonstrate_timeit()


if __name__ == '__main__':
    main()
