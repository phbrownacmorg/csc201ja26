def leapyear(year: int) -> bool:
    """Return True if YEAR is a leap year in the Gregorian calendar; otherwise,
       return False."""
    leap = False # Correct 3/4 of the time
    if (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0):
        leap = True
    return leap

def main(args: list[str]) -> int:
    year = int(input('Please enter a year: '))
    print('The year', year, end=" ")
    if leapyear(year):
        print('is', end=' ')
    else:
        print('is NOT', end=' ')
    print('a leap year')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
