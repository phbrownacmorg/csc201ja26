def main(args: list[str]) -> int:
    # One-argument version: range(STOP)
    # From zero up to (but not including) STOP
    print('range(5):', list(range(5)))
    print('range(10):', list(range(10)))
    # If STOP < 1, the range is empty
    print('range(0):', list(range(0)))
    print('range(-5):', list(range(-5)))
    print()

    # Two-argument version: range(START, STOP):
    # From START up to (but not including) STOP
    print('range(3, 10):', list(range(3, 10)))
    print('range(-3, 10):', list(range(-3, 10)))
    print('range(-10, -3):', list(range(-10, -3)))
    # If START <= STOP, the range is empty
    print('range(-3, -10):', list(range(-3, -10)))

    # Three-argument version: range(START, STOP, STEP)
    # From START by increments of STEP to (but not including) STOP
    print('range(0, 10, 2):', list(range(0, 10, 2))) # Non-negative even numbers less than 10
    print('range(0, 11, 2):', list(range(0, 11, 2))) # Non-negative even numbers through 10
    print('range(0, 101, 5):', list(range(0, 101, 5))) # 0 through 100 by 5's
    print('range(0, 105, 5):', list(range(0, 105, 5))) # Same result for 100 < STOP <= 105
    # You can use this to count down
    print('range(10, -1, -1):', list(range(10, -1, -1))) # Classic rocket countdown

    
    



    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
