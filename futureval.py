def main(args: list[str]) -> int:
    # Read the parameters for an investment
        # Initial amount, interest rate, number of investment periods (months, years, whatever)
    # 1. Accumulator variable
    amt: float = float(input('Please enter an initial amount to invest: ')) 
    rate: float = float(input('Please enter the interest rate, as a percentage: '))
    periods: int = int(input('Please enter the number of periods: '))
    # Print out the parameters
    print('Investing $', amt, ' at ', rate, "% for ", periods, ' periods.', sep="")

    # Change the interest rate from a percentage to a straight value
    rate = rate / 100
    # Make a (rough) table
        # Print the top of the table
    print('Period\tInterest\tBalance')
    print('-' * 40)
        # For each loan period, figure the interest and the new balance, and print them out
    # 2. Loop
    for p in range(periods):
        interest: float = amt * rate
        # 3. Each time through the loop, the accumulator variable gets a little more of the answer
        amt = amt + interest
        print((p+1), '$' + str(round(interest,2)), "", '$' + str(round(amt,2)), sep='\t')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
