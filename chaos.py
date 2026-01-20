import math

def main(args: list[str]) -> int:
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    # Clamp x to the range (0, 1)
    x = max(min(x, 1 - math.ulp(1)), 0 + math.ulp(0))
    print('Initial x:', x)

    for i in range(10): # type: ignore
        x = 3.9 * x * (1 - x)
        print(f'{x:0.10f}')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
