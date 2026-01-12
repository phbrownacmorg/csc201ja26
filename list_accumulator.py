def main(args: list[str]) -> int:
    """Find the sum, average, and product of a list of numbers."""
    # Input: new thing is entering a bunch of values on a single line
    list_string: str = input('Please enter a list of one or more numbers, separated by commas: ')
    #print(list_string)
    string_list: list[str] = list_string.split(',')
    #print(string_list)

    # Accumulator pattern!
    numlist: list[float] = [] # Accumulator variable, initially an empty list
    # Loop
    for s in string_list:
        numlist.append(float(s)) # Update the accumulator variable
    print(numlist)
    
    # Process (accumulator pattern)
    # New thing is multiple accumulator variables in a single loop
    # Type annotations for the *first* use of the three variables
    length: int = 0 # Accumulator variable for length of list
    total: float = 0 # Accumulator variable for sum
    product: float = 1 # Accumulator variable for product

    # Loop
    for num in numlist:
        length = length + 1 # Update the accumulator variable for length
        total = total + num # Update the accumulator variable for sum
        product = product * num # Update the accumulator variable for product
    
    # Output
    print('The sum of the list is', total)
    print('The average of the list is', total/length)
    print('The product of the numbers in the list is', product)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
