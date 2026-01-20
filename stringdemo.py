def show_indexes(s: str) -> None:
    for c in s: # Iterate over the string
        print(c, end=' ')
    print()
    for i in range(len(s)): # Iterate using indices
        print(s[i], end=" ")
    print()
    for i in range(len(s) // 2): 
        print(s[2*i], end=" ") # Indices can be any integer expression
    print()
    for i in range(2*len(s)): 
        print(s[i//2], end=" ") # Indices can be any integer expression
    print()
    for i in range(-1, -2*len(s)-1, -1): 
        print(s[i//2], end=" ") # Indices can be any integer expression
    print()

def show_slicing(s: str) -> None:
    print(s[:]) # Beginning to end
    print(s[:8]) # Up to, but not including, the character in position 8
    print(s[:-4]) # Chops off the last four characters
    print(s[6:9]) # Characters at positions 6, 7, and 8
    print(s[-7:-3]) # Positions -7, -6, -5, and -4
    print(s[4:-2]) # Can mix positive and negative indices
    print(s[1:-1]) # Strip off the two characters at the ends
    print(s[::-1]) # The whole string, but backwards
    print(s[::2]) # Every other character (even indices)
    print(s[1:10:2]) # Every other character (odd indices), except index 11

def main(args: list[str]) -> int:
    s = 'Hello, world'
    print(s)
    show_indexes(s)
    show_slicing(s)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
