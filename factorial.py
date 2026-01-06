def main(args: list[str]) -> int:
    """Find the factorial of a positive integer N, using the accumulator pattern."""
    # Read N
    n: int = int(input('Please enter a positive integer N: '))
    print(n, '! = ', sep="", end="")
    # 1. Accumulator variable
    fact = 1
    # 2. Loop
    for i in range(1, n+1):
        # 3. Update the accumulator variable
        fact = fact * i
    print(fact)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
