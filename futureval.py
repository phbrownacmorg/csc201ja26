from graphics import *

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
    balances: list[float] = [amt] # balances[0] is the initial balance
    # 2. Loop
    for p in range(periods+1):
        interest: float = amt * rate
        # 3. Each time through the loop, the accumulator variable gets a little more of the answer
        amt = amt + interest
        balances.append(amt) # Save the successive amounts in a list

    # Make a (rough) table
        # Print the top of the table
    print('Period\tInterest\tBalance')
    print('-' * 40)
        # Print the initial balance
    print('Initial\t\t\t$', round(balances[0],2), sep='')
    # For each loan period, figure the interest and the new balance, and print them out
    for p in range(1, periods+1):
        interest = balances[p] - balances[p-1]
        print((p), '$' + str(round(interest,2)), "", '$' + str(round(balances[p],2)), sep='\t')

    # Make a graph
    win: GraphWin = GraphWin(title="Investment growth", width=800, height=800)
    max_value = max(balances)
    margin = 0.1
    num_bars = periods+1
    max_X = num_bars * (1 + margin)
    min_X = num_bars * -margin
    max_Y = max_value * (1 + margin)
    min_Y = max_value * -margin
    win.setCoords(min_X, min_Y, max_X, max_Y)

    # Draw axes
    xAxis = Line(Point(0,0), Point(num_bars * (1+(margin/2)), 0))
    xAxis.setArrow('last')
    xAxis.draw(win)
    yAxis = Line(Point(0,0), Point(0, max_value * (1+(margin/2))))
    yAxis.setArrow('last')
    yAxis.draw(win)

    # Draw bars
    for p in range(num_bars):
        bar = Rectangle(Point(p, 0), Point(p+1, balances[p]))
        bar.setFill('green')
        bar.draw(win)

        # label in X
        label = Text(Point(p + 0.5, -0.25 * max_value * margin), str(p))
        label.draw(win)

        # labels in Y.  Spacing tick marks is annoying.  Just put a label on each bar.
        label = Text(Point(p + 0.5, balances[p] + 0.25 * max_value * margin), 
                     '$' + str(round(balances[p])))
        label.draw(win)


    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
