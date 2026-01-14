from graphics import *
from typing import Any

def valid_float(instring: str) -> bool:
    """Returns True if INSTRING contains only a valid positive floating-point
        number in decimal (not exponential) notation, with no thousands 
        separator.  This accepts a proper subset of the floating-point values
        Python accepts."""
    valid = True
    instring = instring.strip() # Get rid of any white space on the ends
    # If the string contains a dot, there can only be one.
    instring = instring.replace('.', '', 1)
    if not instring.isdigit():
        valid = False
    return valid

def valid_int(instring: str) -> bool:
    """Returns True if INSTRING contains only a valid positive base-10 integer,
        with no thousands separator."""
    instring = instring.strip() # Ignore whitespace on the ends
    return instring.isdigit()

def valid_input(amt: float, rate: float, periods: int) -> str:
    msg = ''
    if amt < 0.01:
        msg = 'The amount to invest must be at least $0.01'
    elif rate < 0.0001:
        msg = 'The interest rate must be at least 0.01%'
    elif periods < 1:
        msg = 'The number of periods must be a whole number which is at least 1'
    return msg

def readParameters() -> tuple[float, float, int, str]:
    """Reads the parameters for an investment (amount, interest rate, and the
    number of periods) from the keyboard, and returns them (in that order).  The
    interest rate is returned in absolute terms, not as a percentage."""
    amt, rate, periods = 0, 0, 0
    amt_string = input('Please enter an initial amount to invest: ')
    if amt_string[-1] == '.':
        amt_string = amt_string[:-1]
    if valid_float(amt_string):
        amt = float(amt_string)
        rate_string = input('Please enter the interest rate, as a percentage: ')
        if rate_string[-1] == '.':
            rate_string = rate_string[:-1]
        if valid_float(rate_string):
            rate = float(rate_string)
            rate = rate / 100
            per_string = input('Please enter the number of periods: ')
            if valid_int(per_string):
                periods = int(per_string)
    msg = valid_input(amt, rate, periods)
    if msg == '':
        return amt, rate, periods, msg
    else:
        return 0, 0, 0, msg

def calcBalances(amt: float, rate: float, periods: int) -> list[float]:
    balances: list[float] = [amt] # balances[0] is the initial balance
    # 2. Loop
    for p in range(periods): # type: ignore
        interest: float = amt * rate
        # 3. Each time through the loop, the accumulator variable gets a little more of the answer
        amt = amt + interest
        balances.append(amt) # Save the successive amounts in a list
    return balances

def printTable(balances: list[float]) -> None:
    """Given a list of investment balances BALANCES, print them in a table."""
    # Make a (rough) table
        # Print the top of the table
    print('Period\tInterest\tBalance')
    print('-' * 40)
        # Print the initial balance
    print('Initial\t\t\t$', round(balances[0],2), sep='')
    # For each loan period, figure the interest and the new balance, and print them out
    for p in range(1, len(balances)):
        interest = balances[p] - balances[p-1]
        print((p), '$' + str(round(interest,2)), "", '$' + str(round(balances[p],2)), sep='\t')

def changeCoords(win: GraphWin, top_x: float, top_y: float, margin: float) -> None:
    """Set the coordinates on GraphWin WIN so it will comfortably hold a graph
    contained within the rectangle defined by (0, 0) and (TOP_X, TOP_Y), with
    a margin MARGIN around the edges."""
    max_X = top_x * (1 + margin)
    min_X = top_x * -margin
    max_Y = top_y * (1 + margin)
    min_Y = top_y * -margin
    win.setCoords(min_X, min_Y, max_X, max_Y)

def drawAxes(win: GraphWin, x_end: float, y_end: float) -> None:
    """Draw axes on GraphWin WIN.  The x-axis runs from the origin to (X_END, 0),
        and the y-axis runs from the origin to (0, Y_END)."""
    xAxis = Line(Point(0,0), Point(x_end, 0))
    xAxis.setArrow('last')
    xAxis.draw(win)
    yAxis = Line(Point(0,0), Point(0, y_end))
    yAxis.setArrow('last')
    yAxis.draw(win)

def drawXLabels(win: GraphWin, labels: list[Any], y_offset: float) -> None:
    """On GraphWin WIN, draw X-axis labels from the list LABELS, with an offset
        in y of Y_OFFSET."""
    for i in range(len(labels)):
        label = Text(Point(i + 0.5, y_offset), str(labels[i]))
        label.draw(win)

def drawBars(win: GraphWin, balances: list[float]) -> None:
    """On GraphWin WIN, make bars for a bar graph of the sequence of values BALANCES."""
    for i in range(len(balances)):
        bar = Rectangle(Point(i, 0), Point(i+1, balances[i]))
        bar.setFill('green')
        bar.draw(win)

def labelBars(win: GraphWin, balances: list[float], offset: float) -> None:
    """On GraphWin WIN, create bar labels for bars representing a sequence of
    values BALANCES.  The labels are offset by OFFSET from the top of each
    bar.  The labels are printed with dollar signs."""
    for i in range(len(balances)):
        label = Text(Point(i + 0.5, balances[i] + offset), 
                     '$' + str(round(balances[i])))
        label.draw(win)

def graphBalances(balances: list[float]) -> None:
    """Make a bar graph of a series of investment balances BALANCES, and wait for
    a mouse click.  Because of the wait for a mouse click, this function should be
    called *after* other forms of output have happened."""
    # Prepare the window
    win: GraphWin = GraphWin(title="Investment growth", width=800, height=800)
    max_value = max(balances)
    margin = 0.1
    num_bars = len(balances)
    changeCoords(win, num_bars, max_value, margin)

    # Draw the graph
    drawAxes(win, num_bars * (1+(margin/2)), max_value * (1+(margin/2)))
    drawXLabels(win, list(range(num_bars)), -0.25 * max_value * margin)
    drawBars(win, balances)
    labelBars(win, balances, 0.25 * max_value * margin)

    # Wait for a mouse click
    win.getMouse()
    win.close()

def main(args: list[str]) -> int:
    # Read the parameters for an investment
        # Initial amount, interest rate, number of investment periods (months, years, whatever)
    # 1. Accumulator variable
    amt, rate, periods, err_msg = readParameters()
    if err_msg == '': # Only do the rest if the input is valid
        # Print out the parameters
        print('Investing $', amt, ' at ', (rate*100), "% for ", periods, ' periods.', sep="")
        balances = calcBalances(amt, rate, periods)
        printTable(balances)
        graphBalances(balances)
    else:
        print(err_msg)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
