from andreas_list import AndreasList
from list_of_num import ListOfNum
from list_of_string import ListOfString


def main():
    # Demonstrate ListOfString
    data = ListOfString([11, 2, 22, 4, 105])
    print(f'List Of Strings: {data}')
    print(f'Element At Index 3: {data[3]}')

    # # Append element
    # data.append(192)
    # print(f'List After append(192): {data}')
    #
    # # Extend elements from list
    # data.extend([11, 1.0, True, 'A'])
    # print(f'List After extend({[11, 1.0, True, "A"]}): {data}')
    #
    # # Insert elements at specific index
    # data.insert(5, 5)
    # print(f'List After insert(5, 5): {data}\n')

    # Use __add__, __iadd__ and __radd__ to add elements to the list
    data = data + ['x', 3, 99, 'Hoa', '7', 4]
    print(f'List After (self + ["x", 3, 99, "Hoa", "7", 4]): {data}')

    data += [11, 'A', 0, '17', 9, 44]
    print(f'List After (self += [11, "A", 0, "17", 9, 44]): {data}')

    data2 = ListOfString(['Nice!', 'New String', 123, False])
    print(f'New List Of Strings: {data2}')

    data += data2
    print(f'List After (self += ListOfStrings): {data}')

    # # Demonstrate ListOfNum
    # my_numbers = ListOfNum([1.1, 2, 3j])
    # # my_numbers = ListOfNum([1.1, 3j, 'X'])  # Raises TypeError
    # print(my_numbers)
    #
    # # Append element
    # my_numbers.append(1)
    # # my_numbers.append('4.2')  # Raises TypeError
    # print(my_numbers)
    #
    # # Extend elements from list
    # my_numbers.extend([2.5, 3j, 8])
    # # my_numbers.extend([1.1, '3j', 8.0])  # Raises TypeError
    # print(my_numbers)
    #
    # # Insert elements at specific index
    # my_numbers.insert(2, 99)
    # # my_numbers.insert(2, '99')  # Raises TypeError
    # print(my_numbers)

    # Demonstrate AndreasList
    # stmt = AndreasList(['Welcome', 2, 'Python,', 'Welcome', 'to', 'GÖT'])
    # print(stmt)
    #
    # # Join it to string, without alterning with object
    # print(stmt.join_it())
    #
    # # Map a function on each element
    # print(stmt.map_it(str.upper))
    # print(stmt.map_it(str.lower))
    #
    # # Filter list from predicate, before and after appending 'Post'
    # print(stmt.filter_it(lambda item: item.startswith('P')))
    # stmt.data.append('Post')
    # print(stmt.filter_it(lambda item: item.startswith('P')))
    #
    # # Add function call for each item in list
    # print(stmt.for_each_item(id))
    # stmt.for_each_item(print)


if __name__ == '__main__':
    main()
