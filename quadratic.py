import math # Tells Python we're going to use functions from the math library

def main(args: list[str]) -> int:
    """Program to find the roots of a quadratic system."""
    # Get inputs (a, b, and c define the system)
    print('Please enter the constants a, b, and c for a quadratic ax**2 + bx + c = 0')
    a: float = float(input('a: '))
    b: float = float(input('b: '))
    c: float = float(input('c: '))
    print('The system is ', a, '*x**2 + ', b, '*x + ', c, ' = 0', sep="")

    # Find the roots, if the system has real roots
    determinant: float = math.pow(b,2) - 4*a*c
    # Negative determinant causes a crash right here
    det_root = math.sqrt(determinant)
    root1 = (-b + det_root) / (2*a)
    root2 = (-b - det_root) / (2*a)
    # Print the root(s)
    print('The roots of the system are', root1, 'and', root2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
