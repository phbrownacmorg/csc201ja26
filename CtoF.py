def main(args: list[str]) -> int:
    # Read the Celsius temperature from the keyboard
    degC: float = float(input("Please enter a temperature in Celsius: "))
    # Convert it to Fahrenheit
    degF: float = degC * 1.8 + 32
    # Print out the Fahrenheit temperature
    print(degC, '\u00b0 C = ', end='', sep="")
    print(degF, '\u00b0 F', sep="")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
