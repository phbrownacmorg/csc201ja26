from typing import Any

def show_operations() -> None:
    a_list: list[Any] = ['a', 2, ['3', 4], True]
    a_tuple: tuple[Any,...] = tuple(a_list)
    print(a_list, a_tuple)
    
    # Lists are mutable
    a_list[0] = 1
    a_list[2][1] = "another value" # Note the aliasing with a_tuple[2]!
    a_list.append(False)
    print(a_list, a_tuple)

    # Tuples are immutable, except when they hold mutable objects
    #a_tuple[1] = 'two' # Undefined
    a_tuple[2][0] = 3
    print(a_list, a_tuple)

    # Subscripting within items
    print(a_list[2][1][-5:]) # Slice from a string, within a list, within a list

    # List/tuple slicing: slice of a list is a list, slice of a tuple is a tuple,
    #   (just as a slice of a string is a string)
    print(a_list[3:], a_tuple[:2], a_tuple[2][1][2:7])

    # Concatenation
    print(a_list + list(a_tuple))  # Concatenating lists
    print(tuple(a_list) + a_tuple) # Concatenating tuples also works

    # Iterating over a sequence
    for item in a_tuple:
        print(item, end='; ')
    print()

    # Iterating over a sequence by index
    for i in range(len(a_tuple)):
        print(a_tuple[i], end='; ')
    print()

    # Membership
    for item in a_list:
        print(item, item in a_tuple, item not in a_tuple)

    for i in range(26):
        letter = chr(97+i)
        print(letter, letter in a_list[2][1])

def show_list_comprehensions() -> None:
    # Squares of numbers up to 10
    print([x**2 for x in range(10)])

    # Squares of odd numbers up to 10
    print([(x, x**2) for x in range(10) if x % 2 != 0 and (x - 1) % 4 == 0])

    a_list: list[Any] = ['a', 2, ['3', 4], True]
    print([c.upper() for c in a_list if type(c) == type('')])

def show_popping() -> None:
    num_list = list(range(4, 12))
    print(num_list)
    # Pop off the back
    print(num_list.pop(), num_list)
    # Pop off the front
    print(num_list.pop(0), num_list)
    # Pop from the middle
    print(num_list.pop(3), num_list)

    # Empty a list by repeated pops
    for i in range(len(num_list)):
        print((i, num_list.pop()), end='\t')
    print(num_list) # Empty list

def main(args: list[str]) -> int:
    show_operations()
    show_list_comprehensions()
    show_popping()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
