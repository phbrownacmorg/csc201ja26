import math # Tells Python we're going to use functions from the math library

def readConstants() -> tuple[float, float, float]:
    """Read and return the constants a, b, and c of a quadratic system from the keyboard."""
    print('Please enter the constants a, b, and c for a quadratic ax**2 + bx + c = 0')
    a: float = float(input('a: '))
    b: float = float(input('b: '))
    c: float = float(input('c: '))
    return a, b, c

def determinant(a: float, b: float, c: float) -> float:
    return math.pow(b,2) - 4*a*c

def findRoots(a: float, b: float, c: float) -> tuple[float, float]:
    """Find the roots of the quadratic system A*x**2 + B*x + C = 0, if the
        system has real roots.  If the roots are not real, return math.nan
        for both."""
    det = determinant(a, b, c)
    # Negative determinant causes a crash right here
    if det < 0:
        root1, root2 = math.nan, math.nan
    else: # det >= 0, roots are real
        det_root = math.sqrt(det)
        root1 = (-b + det_root) / (2*a)
        root2 = (-b - det_root) / (2*a)
    return root1, root2

def main(args: list[str]) -> int:
    """Program to find the roots of a quadratic system."""
    a, b, c = readConstants()
    print('The system is ', a, '*x**2 + ', b, '*x + ', c, ' = 0', sep="")

    root1, root2 = findRoots(a, b, c)
    if math.isnan(root1): # Only have to test root1.  If one root is imaginary, they both are.
        print('The system has no real roots.')
    else:
        print('The roots of the system are', root1, 'and', root2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
