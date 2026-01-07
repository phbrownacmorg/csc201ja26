import math

def main(args: list[str]) -> int:
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    # Clamp x to the range (0, 1)
    x = max(min(x, 1 - math.ulp(1)), 0 + math.ulp(0))
    print('Initial x:', x)

    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
