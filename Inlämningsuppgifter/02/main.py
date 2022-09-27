from list_of_strings import ListOfStrings


def main():
    original = [11, 2, 22, 4, 105]
    print(f'Original List: {original}')

    data = ListOfStrings(original)
    print(f'List Of Strings: {data}')
    print(f'Element At Index 3: {data[3]}')

    data.extend([11, 1.0, True, 'A'])
    print(f'List After extend({[11, 1.0, True, "A"]}): {data}')

    data.append(192)
    print(f'List After append(192): {data}')

    data.insert(5, 5)
    print(f'List After insert(5, 5): {data}\n')

    data = data + ['x', 3, 99] + 4
    print(f'List After (self + ["x", 3, 99] + 4): {data}')

    data += [11, 'A', 0]
    print(f'List After (self += [11, "A", 0]): {data}')

    data2 = ListOfStrings(['Nice!', 'New String', 123, False])
    print(f'New List Of Strings: {data2}')

    data += data2
    print(f'List After (self += ListOfStrings): {data}')
    print(data2)


if __name__ == '__main__':
    main()
