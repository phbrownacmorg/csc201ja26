def printChaosTable(x: float, n: int) -> None:
    print(f'{'n':^3}\t{'x':^12}')
    print('-' * 20)
    print(f'{'0':>2}\t{x:0.10f}')
    for i in range(n): # type: ignore
        x = 3.9 * x * (1 - x)
        print(f'{i+1:>2}\t{x:0.10f}')
    print()

def writeChaosTables(outfilename: str, 
                     results: list[list[float]]) -> None:
    with open(outfilename, 'w') as f:
        for r in results:
            f.write(f'{'n':^3}\t{'x':^12}\n')
            f.write('-' * 20 + '\n')
            f.write(f'{'0':>2}\t{r[0]:0.10f}\n')
            for i in range(1, len(r)): # type: ignore
                f.write(f'{i:>2}\t{r[i]:0.10f}\n')
            f.write('\n')

def runInteractively() -> None:
    try:
        while True:
            x = float(input("Enter a number between 0 and 1: "))
            #print('Initial x:', x)
            n = int(input('Enter the number of iterations: '))
            printChaosTable(x, n)
    except ValueError:
        pass

def readScenarios(infilename: str) -> list[tuple[float, int]]:
    result: list[tuple[float, int]] = []
    linenum = 0
    with open(infilename) as f:
        for line in f.readlines(): # One scenario per line
            linenum = linenum + 1
            errmsg = f'Error on line {linenum}: '
            numbers = line.split(',')
            if len(numbers) != 2:
                print(errmsg + 'line does not have two numbers')
                continue
            try:
                x = float(numbers[0])
                n = int(numbers[1])
                if not (0 < x < 1):
                    raise ValueError('value of x is outside the range (0, 1).')
                elif n < 0:
                    raise ValueError('value of n cannot be negative.')
            except ValueError as e:
                if e.args[0].startswith('value of '):
                    print(errmsg + e.args[0])
                else:
                    print(errmsg + 'number cannot be read.')
                continue
            else:
                result.append( (x, n) )
    return result

def calculateChaos(x: float, n: int) -> list[float]:
    result: list[float] = [x]
    for i in range(n): # type: ignore
        x = 3.9 * x * (1 - x)
        result.append(x)
    return result

def runFromFiles(infilename: str, outfilename: str) -> None:
    # Read scenarios
    scenarios: list[tuple[float, int]] = readScenarios(infilename)
    chaotic_results: list[list[float]] = []
    for s in scenarios:
        chaotic_results.append(calculateChaos(s[0], s[1]))
    writeChaosTables(outfilename, chaotic_results)

def main(args: list[str]) -> int:
    print("This program illustrates a chaotic function")
    #runInteractively()
    runFromFiles('chaos-seeds.csv', 'chaos_out.txt')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
