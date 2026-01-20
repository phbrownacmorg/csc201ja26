def definite_loop(iterations: int) -> list[int]:
    num_list: list[int] = []
    for i in range(1, iterations+1):
        num_list.append(i**3)
    return num_list

def indefinite_definite_loop(iterations: int) -> list[int]:
    num_list: list[int] = []
    i = 1
    while i <= iterations:
        num_list.append(i**3)
        i = i+1 # <- Very important!! (and easy to forget)
    return num_list

def interactive_loop() -> list[int]:
    num_list: list[int] = []
    response: str = 'Y'
    while response != 'n':
        num_list.append(int(input('Please enter a whole number: ')))
        response = input('Would you like to input another? [Y/n]: ').strip().lower() # This can get annoying
        if len(response) > 0: # Reduce the response to just the first letter
            response = response[0]
    return num_list

def sentinel_loop() -> list[int]:
    """Classic sentinel loop, using a particular special value of the same type as the entries."""
    num_list: list[int] = []
    sentinel = -9999
    prompt = 'Please enter a whole number, or ' + str(sentinel) + ' to exit: '
    response = int(input(prompt)) # Read the first value
    while response != sentinel:
        num_list.append(response)
        response = int(input(prompt))
    return num_list

def sentinel_loop_using_exception() -> list[int]:
    num_list: list[int] = []
    try:
        while True:
            # Raises ValueError when the user enters anything else
            num_list.append(int(input('Please enter an integer, or Enter to exit: ')))
    except ValueError:
        return num_list

def nested_loop() -> list[int]:
    num_list: list[int] = []
    prompt = 'Please enter one or more integers separated by spaces, or a non-integer to exit: '
    try:
        while True:
            num_string = input(prompt)
            line_strings = num_string.split() # Get each integer by itself, still as a string
            for s in line_strings:
                num_list.append(int(s))
    except ValueError:
        return num_list

def main(args: list[str]) -> int:
    print(definite_loop(10))
    print(indefinite_definite_loop(10)) # Should be the same
    #print(interactive_loop())
    #print(sentinel_loop())
    print(sentinel_loop_using_exception())
    print(nested_loop())

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
