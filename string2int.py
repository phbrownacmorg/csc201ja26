def str2int(s: str) -> int:
    s = s.strip()  # Get rid of spaces at the ends
    # Remove common separators
    s = s.replace(',','') # commas
    s = s.replace(' ',"") # internal spaces
    s = s.replace('.','') # dots (may give unexpected results if a float is entered)

    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:] # Just leave the digits

    if not s.isdigit():
        raise ValueError(f'"{s}" cannot be converted to an integer.') # Raise the error, if there will be one
    result = 0
    for c in s:
        digitvalue = (ord(c) - ord('0'))
        result = 10*result + digitvalue
    return sign * result

def main(args: list[str]) -> int:
    in_string = input('Please enter an integer: ') # It's still a string
    print('"' + in_string + '"', type(in_string))
    n = str2int(in_string)
    print(n, type(n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
